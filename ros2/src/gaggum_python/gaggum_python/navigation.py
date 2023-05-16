import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry, Path

class Navigation(Node):
    def __init__(self):
        super().__init__('navigation')
    # subscriber-----------------------------------
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.plan_sub = self.create_subscription(Path, '/plan', self.plan_callback, 10)
        self.twist_sub = self.create_subscription(Twist, '/cmd_vel', self.twist_callback, 10)
    
    # publisher------------------------------------
        self.goal_pose_pub = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.twist_pub = self.create_publisher(Twist, '/cmd_vel', 10)

    # timer_callback
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    # 상태------------------------------------------
        self.is_odom = False    # Odometry
        self.is_plan = False    # Path
        self.is_move = True     # 터틀봇이 이동 가능한 상태
        self.is_twist = False   # Twist

    # 메시지------------------------------------------
        self.pose_msg = PoseStamped()   # nav2에 목표 좌표 보냄
        self.odom_msg = Odometry()      # odom
        self.plan_msg = Path()          # 터틀봇의 이동 경로 좌표
        self.twist_msg = Twist()        # 터틀봇 움직임 제어

    # 데이터----------------------------------------
        
        # 백에서 넘어오는 trigger 더미
        self.triggers = {
            'data': [
                {'plant_number': 3, 'plant_original_name': 'plant3', 'plant_position_x': 1.5023, 'plant_position_y': 0.9781},
            ],
            'mode': 100  
            # 'data': [
            #     {'plant_number': 1, 'plant_original_name': 'plant1', 'plant_position_x': -4.87, 'plant_position_y': 3.48},
            #     {'plant_number': 2, 'plant_original_name': 'plant2', 'plant_position_x': -2.92, 'plant_position_y': 3.49}
            # ],
            # 'mode': 200,
            # 'sunSpots': [
            #     {'sunspot_number': 0, 'sunspot_isplant': 0, 'sunspot_x_position': 0, 'sunspot_y_position': 0},
        }

    def timer_callback(self):

        if self.is_move:
            self.pose_msg.header.frame_id = "map"
            # 터틀봇의 위치
            # self.pose_msg.pose.position.x = self.triggers['data']['plant_position_x']
            # self.pose_msg.pose.position.y = self.triggers['data']['plant_position_y']
            self.pose_msg.pose.position.x = 0.0
            self.pose_msg.pose.position.y = 0.0

            # 터틀봇의 방향
            self.pose_msg.pose.orientation.x = 0.0
            self.pose_msg.pose.orientation.y = 0.0
            self.pose_msg.pose.orientation.w = 1.0
            print(self.is_twist)

            
            if self.is_plan:
                position = self.plan_msg.poses[0].pose.position
                # 대략 0.2 정도의 오차가 발생함
                # print(position.x, position.y)
                # 목표 지점 1 범위 이내에 들어왔으면
                x = self.pose_msg.pose.position.x
                y = self.pose_msg.pose.position.y

                if x - 1 < position.x < x + 1 and y -1 < position.y <  y + 1:
                    print("목표 지점 도착")
                    self.is_plan = False
                    self.is_move = False

            # 메시지 publish 부분
            self.goal_pose_pub.publish(self.pose_msg)
            
            # 터틀봇의 속도
            self.twist_msg.linear.x = 0.05
            self.twist_pub.publish(self.twist_msg)
            
            # 코드 상태 확인용 print
            print('Publishing: "%s"' % self.pose_msg.pose.position)

        else:
            print('터틀봇 멈춤')
            if self.triggers['mode'] == 100:
                print('물 주기')
                # 물 주기 노드에 publish
            elif self.triggers['mode'] == 200:
                print('햇빛 이동')

    # callback 함수 ------------------------
    def odom_callback(self, msg):
        self.is_odom = True
        self.odom_msg = msg
    
    def plan_callback(self, msg):
        self.is_plan = True
        self.plan_msg = msg # 이동 좌표가에 담겨있음

    def twist_callback(self, msg):
        self.is_twist = True
        self.twist_msg = msg

def main(args=None):
    rclpy.init(args=args)

    navigation = Navigation()

    rclpy.spin(navigation)

    navigation.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()