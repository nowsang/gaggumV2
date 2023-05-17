import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped, Twist
from gaggum_msgs.msg import Detection
from nav_msgs.msg import Odometry, Path
from std_msgs.msg import Int16

class Navigation(Node):
    def __init__(self):
        super().__init__('navigation')
    # subscriber-----------------------------------
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.plan_sub = self.create_subscription(Path, '/plan', self.plan_callback, 10)
        self.twist_sub = self.create_subscription(Twist, '/cmd_vel', self.twist_callback, 10)
        self.yolo_sub = self.create_subscription(Detection, '/yolo_detected', self.yolo_callback, 10)

    # publisher------------------------------------
        self.goal_pose_pub = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.twist_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.water_pub = self.create_publisher(Int16, '/water', 10)
        self.move_sun_pub = self.create_publisher(Int16, '/move_sun', 10)

    # timer_callback
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    # 상태------------------------------------------
        self.is_odom = False            # Odometry
        self.is_plan = False            # Path
        self.is_move = True             # 터틀봇이 이동 가능한 상태
        self.is_twist = False           # Twist
        self.is_yolo = False            # yolo
        self.is_plant_detected = False  # 화분 감지 확인

    # 메시지------------------------------------------
        self.pose_msg = PoseStamped()   # nav2에 목표 좌표 보냄
        self.odom_msg = Odometry()      # odom
        self.plan_msg = Path()          # 터틀봇의 이동 경로 좌표
        self.twist_msg = Twist()        # 터틀봇 움직임 제어
        self.water_msg = Int16()        # 물 주라는 메시지
        self.move_sun_msg = Int16()     # 햇빛 이동
        self.yolo_msg = Detection()

    # 데이터------------------------------------------
        # 백에서 넘어오는 데이터 더미
        self.plant_datas = {
            'data': [
                {'plant_id': 3, 'plant_detected_name': 'plant3', 'plant_position_x': 1.5023, 'plant_position_y': 0.9781,},
            ],
            'mode': 100  
            # 'data': [
            #     {'plant_id': 1, 'plant_detected_name': 'plant1', 'plant_position_x': -4.87, 'plant_position_y': 3.48},
            #     {'plant_id': 2, 'plant_detected_name': 'plant2', 'plant_position_x': -2.92, 'plant_position_y': 3.49}
            # ],
            # 'mode': 200,
            # 'sunSpots': [
            #     {'sunspot_number': 0, 'sunspot_isplant': 0, 'sunspot_x_position': 0, 'sunspot_y_position': 0},
        }
        self.plant_id = 0
        self.plant_detected_name = ''
        self.goal_x = 0
        self.goal_y = 0
        self.plant_name = ''

        self.plant_id = self.plant_datas['data'][0]['plant_id']
        self.plant_detected_name = self.plant_datas['data'][0]['plant_detected_name']
        self.goal_x = self.plant_datas['data'][0]['plant_position_x']
        self.goal_y = self.plant_datas['data'][0]['plant_position_y']


        # yolo 관련
        self.yolo_distance = 10     # 화분과의 거리
        self.yolo_number = 0        # 화분의 번호
        self.yolo_cx = 0            # 화분의 중심 x좌표
        self.yolo_cy = 0            # 화분의 중심 y좌표
        self.yolo_view_width = 640  # 카메라 이미지의 넓이
        self.tolerance = 3          # 중심 맞추기 오차 허용치


    def timer_callback(self):
        
        if self.is_odom and self.is_yolo and self.is_twist: # 시작 조건 odom, yolo, twist의 값이 넘어올 때
        
            if self.is_move:    # 터틀봇이 이동 가능한 상태

                if self.is_plan:    # 목표 좌표가 넘어오면
                    self.pose_msg.header.frame_id = "map"
                    # 터틀봇의 목표 위치
                    # self.pose_msg.pose.position.x = self.triggers['data']['plant_position_x']
                    # self.pose_msg.pose.position.y = self.triggers['data']['plant_position_y']
                    self.pose_msg.pose.position.x = 1.3
                    self.pose_msg.pose.position.y = 0.5
                    # self.pose_msg.pose.position.x = -0.7
                    # self.pose_msg.pose.position.y = 1.9

                    # 터틀봇의 방향
                    self.pose_msg.pose.orientation.x = 0.0
                    self.pose_msg.pose.orientation.y = 0.0
                    self.pose_msg.pose.orientation.w = 1.0
                    position = self.plan_msg.poses[0].pose.position
                    # 대략 0.2 정도의 오차가 발생함
                    # print(position.x, position.y)
                    x = self.pose_msg.pose.position.x
                    y = self.pose_msg.pose.position.y
                    
                    # 목표 지점 1 범위 이내에 들어왔으면
                    if x - 0.1 < position.x < x + 0.1 and y -0.1 < position.y <  y + 0.1:
                        print("목표 지점 도착")
                        self.is_plan = False
                        self.is_move = False
                    else:            
                        # 화분이 0.5 거리 이내에 감지되면
                        if self.yolo_distance <= 0.5:
                            print("화분 감지")
                            if  self.yolo_number == self.plant_number - 1:  # 목표 화분인지 확인
                                self.is_plan = False
                                self.is_move = False
                                self.is_plant_detected = True 

                    self.goal_pose_pub.publish(self.pose_msg)               
                
                # 코드 상태 확인용 print
                print('Publishing: "%s"' % self.pose_msg.pose.position)

            else:
                # 터틀봇을 멈춘 상태
                self.twist_msg.linear.x = 0.0
                self.twist_msg.angular.z = 0.0
                print('터틀봇 멈춤')

                if self.is_plant_detected:      # 식물이 감지 되었으면
                    self.centerPositioning()    # 중심 맞추기

                if self.triggers['mode'] == 100:
                    print('물 주기')
                    # 물 주기 노드에 publish
                    self.water_msg.data = 1
                    self.water_pub.publish(self.water_msg)

                elif self.triggers['mode'] == 200:
                    print('햇빛 이동')
                    self.move_sun_msg.data = 1
                    self.move_sun_pub.publish(self.move_sun_msg)
            
            self.twist_pub.publish(self.twist_msg)
            
            

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

    def yolo_callback(self, msg):
        self.is_yolo = True
        self.yolo_msg = msg

        # yolo 변수 할당
        idx = self.yolo_msg.object_class.index(self.plan_number - 1)
        self.yolo_distance = self.yolo_msg.distance[idx]
        self.yolo_number = self.yolo_msg.object_class[idx]
        self.yolo_cx = self.yolo_msg.cx[idx]
        self.yolo_cy = self.yolo_msg.cy[idx]
    
    # 커스텀 함수 ---------------------------
    def centerPositioning(self):
        point = self.yolo_view_width    
        min_x = self.yolo_view_width - self.tolerance
        max_x = self.yolo_view_width + self.tolerance
        

        if min_x <= self.yolo_cx <= max_x:        # 중심 좌표가 허용치 내에 있으면
            self.twist_msg.linear.x = 0.01        # 천천히 전진
            self.twist_msg.angular.z = 0.0  
        else:                                     # 중심이 안 맞으면
            if self.yolo_cx < point - 5:          # 중심이 왼쪽에 있으면  
                self.twist_msg.angular.z = -0.01  # 왼쪽으로 회전           
            else:                                 # 중심이 오른쪽에 있으면
                self.twist_msg.angular.z = 0.01   # 오른쪽으로 회전



def main(args=None):
    rclpy.init(args=args)

    navigation = Navigation()

    rclpy.spin(navigation)

    navigation.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()