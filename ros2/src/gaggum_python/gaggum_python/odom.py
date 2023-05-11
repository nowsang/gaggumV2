import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from gaggum_msgs.msg import TurtlebotStatus
from sensor_msgs.msg import Imu
from squaternion import Quaternion
from nav_msgs.msg import Odometry
from math import pi,cos,sin
import tf2_ros
import geometry_msgs.msg
import time

# odom 노드는 로봇의 속도(/turtlebot_status), Imu센서(/imu) 메시지를 받아서 로봇의 위치를 추정하는 노드입니다.
# sub2_odom에서는 로봇의 키네마틱스를 풀면 로봇의 선속도, 각속도를 이용해 로봇의 포즈를 추정할 할 것입니다.
# 작성한 sub1_odom 와 sub2_odom 중 오차가 가장 적은 방법을 사용하세요.


# 노드 로직 순서
# 1. publisher, subscriber, broadcaster 만들기
# 2. publish, broadcast 할 메시지 설정
# 3. 로봇 위치 추정
# 4. 추정한 로봇 위치를 메시지에 담아 publish, broadcast

class odom(Node):

    def __init__(self):
        super().__init__('odom')
        
        # 로직 1. publisher, subscriber, broadcaster 만들기
        self.subscription = self.create_subscription(Twist,'/cmd_vel',self.listener_callback,10)
        self.imu_sub = self.create_subscription(Imu,'/imu',self.imu_callback,10)
        self.odom_publisher = self.create_publisher(Odometry, 'odom', 10)
        self.broadcaster = tf2_ros.StaticTransformBroadcaster(self)


        # 로봇의 pose를 저장해 publish 할 메시지 변수 입니다.
        self.odom_msg=Odometry()
        # Map -> base_link 좌표계에 대한 정보를 가지고 있는 변수 입니다.
        self.base_link_transform=geometry_msgs.msg.TransformStamped()
        # base_link -> laser 좌표계에 대한 정보를 가지고 있는 변수 입니다.
        self.laser_transform=geometry_msgs.msg.TransformStamped()
        self.is_status=False
        self.is_imu=False
        self.is_calc_theta=False
        # x,y,theta는 추정한 로봇의 위치를 저장할 변수 입니다.        
        # 로봇의 초기위치를 맵 상에서 로봇의 위치와 맞춰줘야 합니다.
        self.x = -5.818
        self.y = 6.398
        self.theta=0.0
        # imu_offset은 초기 로봇의 orientation을 저장할 변수 입니다.
        self.imu_offset=0
        self.prev_time=0
 
        
        '''
        로직 2. publish, broadcast 할 메시지 설정
        '''
        self.odom_msg.header.frame_id = 'map'
        self.odom_msg.child_frame_id = 'base_link'

        self.base_link_transform.header.frame_id = 'map'
        self.base_link_transform.child_frame_id = 'base_link'

        self.laser_transform.header.frame_id = 'base_link'
        self.laser_transform.child_frame_id = 'laser'
        self.laser_transform.transform.translation.x = 0.0
        self.laser_transform.transform.translation.y = 0.0
        self.laser_transform.transform.translation.z = 0.19
        self.laser_transform.transform.rotation.w = 1.0
    
    def imu_callback(self,msg):
       
        #로직 3. IMU 에서 받은 quaternion을 euler angle로 변환해서 사용

        if self.is_imu == False:
            self.is_imu = True
            imu_q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
            # self.imu_offset = imu_q.to_euler()[2]  라이다 고정 안됨
            e = imu_q.to_euler()
            self.imu_offset = e[2]
        else:
            imu_q = Quaternion(msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z)
            e = imu_q.to_euler()
            self.theta = e[2]
            
    def listener_callback(self, msg):
        print('linear_vel : {}  angular_vel : {}'.format(msg.twist.linear.x,-msg.twist.angular.z))
        if self.is_imu == True:
            if self.is_status == False :
                self.is_status = True
                self.prev_time=rclpy.clock.Clock().now()
            else :
                
                self.current_time=rclpy.clock.Clock().now()
                # 계산 주기를 저장한 변수 입니다. 단위는 초(s)
                self.period=(self.current_time-self.prev_time).nanoseconds/1000000000
                # 로봇의 선속도, 각속도를 저장하는 변수, 시뮬레이터에서 주는 각 속도는 방향이 반대이므로 (-)를 붙여줍니다.
                linear_x = msg.twist.linear.x
                angular_z = -msg.twist.angular.z
                '''
                로직 3. 로봇 위치 추정
                (테스트) linear_x = 1, self.theta = 1.5707(rad), self.period = 1 일 때
                self.x=0, self.y=1 이 나와야 합니다. 로봇의 헤딩이 90도 돌아가 있는
                상태에서 선속도를 가진다는 것은 x축방향이 아니라 y축방향으로 이동한다는 뜻입니다. 
                #절대위치 사용
                '''
                self.x += linear_x * cos(self.theta) * self.period
                self.y += linear_x * sin(self.theta) *self.period
                self.theta += angular_z * self.period

                self.base_link_transform.header.stamp =rclpy.clock.Clock().now().to_msg()
                self.laser_transform.header.stamp =rclpy.clock.Clock().now().to_msg()
                
                '''
                로직 4. 추정한 로봇 위치를 메시지에 담아 publish, broadcast
                '''
                q = Quaternion.from_euler(0, 0, self.theta)
                
                self.base_link_transform.transform.translation.x = self.x
                self.base_link_transform.transform.translation.y = self.y
                self.base_link_transform.transform.rotation.x = q.x
                self.base_link_transform.transform.rotation.y = q.y
                self.base_link_transform.transform.rotation.z = q.z
                self.base_link_transform.transform.rotation.w = q.w
                
                self.odom_msg.pose.pose.position.x=self.x
                self.odom_msg.pose.pose.position.y=self.y
                self.odom_msg.pose.pose.orientation.x=q.x
                self.odom_msg.pose.pose.orientation.y=q.y
                self.odom_msg.pose.pose.orientation.z=q.z
                self.odom_msg.pose.pose.orientation.w=q.w
                self.odom_msg.twist.twist.linear.x=linear_x
                self.odom_msg.twist.twist.angular.z=angular_z

         

                self.broadcaster.sendTransform(self.base_link_transform)
                self.broadcaster.sendTransform(self.laser_transform)
                self.odom_publisher.publish(self.odom_msg)
                self.prev_time=self.current_time

        
def main(args=None):
    rclpy.init(args=args)

    sub2_odom = odom()

    rclpy.spin(sub2_odom)


    sub2_odom.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
