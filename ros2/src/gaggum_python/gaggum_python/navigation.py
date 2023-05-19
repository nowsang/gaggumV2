import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped, Twist
from gaggum_msgs.msg import Detection
from nav_msgs.msg import Odometry, Path
from std_msgs.msg import Int16, Int32
import time
from rclpy.duration import Duration
# from nav2_simple_commander.robot_navigator import BasicNavigator

class Navigation(Node):
    def __init__(self):
        super().__init__('navigation')
    # subscriber-----------------------------------
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.plan_sub = self.create_subscription(Path, '/plan', self.plan_callback, 10)
        self.twist_sub = self.create_subscription(Twist, '/cmd_vel', self.twist_callback, 10)
        self.yolo_sub = self.create_subscription(Detection, '/yolo_detected', self.yolo_callback, 10)
        self.sonar_sub = self.create_subscription(Int32, 'sonar', self.sonar_callback, 10)

    # publisher------------------------------------
        self.goal_pose_pub = self.create_publisher(PoseStamped, '/goal_pose', 100)
        self.twist_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.motor_pub = self.create_publisher(Int32, '/motor', 100)

    # timer_callback
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    # 상태------------------------------------------
        self.is_odom = False            # Odometry
        self.is_plan = False            # Path
        self.is_path_tracking = True    # 터틀봇이 경로를 따라가는 중
        self.is_twist = False           # Twist
        self.is_yolo = False            # yolo
        self.is_plant_detected = False  # 화분 감지 확인
        self.is_center = False          # 중앙 정렬
        self.is_sonar = False           # 초음파 센서
        self.is_approch = False         # 화분에 근접
        self.is_working = True
        

    # 메시지------------------------------------------
        self.pose_msg = PoseStamped()   # nav2에 목표 좌표 보냄
        self.odom_msg = Odometry()      # odom
        self.plan_msg = Path()          # 터틀봇의 이동 경로 좌표
        self.twist_msg = Twist()        # 터틀봇 움직임 제어
        # self.water_msg = Int16()        # 물 주라는 메시지
        # self.move_sun_msg = Int16()     # 햇빛 이동
        self.yolo_msg = Detection()
        self.motor_msg = Int32()

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
        self.yolo_distance = 999    # 화분과의 거리
        self.yolo_number = 0        # 화분의 번호
        self.yolo_cx = 0            # 화분의 중심 x좌표
        self.yolo_cy = 0            # 화분의 중심 y좌표
        self.yolo_view_width = 640  # 카메라 이미지의 넓이


        # plan
        self.pose_msg.pose.position.x = 1.5
        self.pose_msg.pose.position.y = 0.16
        self.pose_msg.pose.orientation.z = 0.0
        self.pose_msg.header.frame_id = "map"

        self.count  = 0
        self.water_cnt = 0

    def timer_callback(self):
        print(self.is_odom, self.is_yolo, self.is_plan, self.is_path_tracking, self.is_twist)
        if self.is_odom and self.is_yolo and self.is_twist: # 시작 조건 odom, yolo, twist의 값이 넘어올 때
            if self.is_path_tracking:    # 터틀봇이 길따라 가는 중

                if self.is_plan:    # 목표 좌표가 넘어오면
                    
                    position = self.plan_msg.poses[0].pose.position
                    # 대략 0.2 정도의 오차가 발생함
                    # print(position.x, position.y)
                    x = self.pose_msg.pose.position.x
                    y = self.pose_msg.pose.position.y

                    # 목표 지점 1 범위 이내에 들어왔으면
                    if x - 0.4 < position.x < x + 0.4 and y - 0.4 < position.y <  y + 0.4:
                        print("목표 지점 도착")
                        self.is_path_tracking = False
                        self.is_plan = False

                self.goal_pose_pub.publish(self.pose_msg)               
                
                # 코드 상태 확인용 print
                print('Publishing: "%s"' % self.pose_msg.pose.position)

            else:
                print(self.is_working)
                if self.is_working:
                    print("화분과의 거리:",self.yolo_distance)
                    # 화분에 접근하는 거
                    print("화분 감지")
                    if self.yolo_distance <= 400: 
                        if self.is_center:                      # 중심 맞춰지면
                            self.twist_msg.linear.x = 0.05      # 전진 
                            self.twist_msg.angular.z = 0.0 
                            
                            print(self.sonar_distance)
                            if self.sonar_distance <= 27:  # 근접하면
                                print('근접 완료')
                                self.twist_msg.linear.x = 0.05
                                self.twist_pub.publish(self.twist_msg)
                                time.sleep(3.5) 
                                self.twist_msg.linear.x = 0.0
                                self.is_approch = True
                            elif self.sonar_distance <= 25:
                                self.twist_msg.linear.x = - 0.1
                        else:                                  
                            self.centerPositioning()            # 중심 맞추기
                    else:                                       # 식물이 감지 되지 않음
                        self.twist_msg.angular.z = 0.2          # 제자리 회전
                    
                    # 접근 했을 때
                    if self.is_approch:
                        if self.plant_datas['mode'] == 100 and self.water_cnt < 1:
                            print('물 주기')
                            self.motor_msg.data = 1
                            self.motor_pub.publish(self.motor_msg)
                            print('물 주는 중')
                            self.water_cnt += 1
                            time.sleep(8.0)
                            
                            print('화분 드는 중')
                            self.motor_msg.data = 2
                            self.motor_pub.publish(self.motor_msg)
                            time.sleep(7.0)

                            self.moveSunPoint()

                            self.is_path_tracking = True
                            self.is_plan = True
                            
                        else:
                            print('화분 내리는 중')
                            time.sleep(5.0)
                            self.motor_msg.data = 3
                            self.motor_pub.publish(self.motor_msg)
                            time.sleep(10.0)

                            self.moveStartPoint()
                            self.is_working = False

                else:
                    print('뒤로 가는 중:', self.sonar_distance)
                    self.twist_msg.linear.x = -0.1
                    if self.sonar_distance > 250:
                        self.twist_msg.linear.x = 0.0
                        self.is_path_tracking = True
        
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
        # idx = self.yolo_msg.object_class.index(self.plant_number - 1)
        try:
            idx = 0
            self.yolo_distance = self.yolo_msg.distance[idx]
            self.yolo_number = self.yolo_msg.object_class[idx]
            self.yolo_cx = self.yolo_msg.cx[idx]
            self.yolo_cy = self.yolo_msg.cy[idx]
        except:
            pass

    def sonar_callback(self, msg):
        self.is_sonar = True
        if msg.data < 500:
            self.sonar_distance = msg.data

    # 커스텀 함수 ---------------------------
    def centerPositioning(self):
        print('중심을 맞추자') 
        center = 338
        min_x = center - 2
        max_x = center + 2
        
        print(min_x,'<=', self.yolo_cx, '<=', max_x)
        if min_x <= self.yolo_cx <= max_x:        # 중심 좌표가 허용치 내에 있으면
            self.count += 1
            print('중앙 정렬', self.count)
            self.twist_msg.angular.z = 0.0
            if self.count > 5:
                self.is_center = True
                print('중앙 정렬 완료')
                return
        else:                                     # 중심이 안 맞으면
            if self.yolo_cx < min_x:              # 중심이 왼쪽에 있으면  
                self.twist_msg.angular.z = 0.1    # 왼쪽으로 회전    
                if self.yolo_cx < min_x - 60:
                    self.twist_msg.angular.z = 0.3    # 왼쪽으로 회전 

            elif self.yolo_cx > max_x:            # 중심이 오른쪽에 있으면
                self.twist_msg.angular.z = - 0.1  # 오른쪽으로 회전
                if self.yolo_cx > min_x + 60:
                    self.twist_msg.angular.z = - 0.3    # 왼쪽으로 회전 

    def moveStartPoint(self):
        self.pose_msg.pose.position.x = 0.0
        self.pose_msg.pose.position.y = 0.0
        self.pose_msg.pose.orientation.z = 0.0
    
    def moveSunPoint(self):
        self.pose_msg.pose.position.x = 1.0
        self.pose_msg.pose.position.y = 1.27
        self.pose_msg.pose.orientation.z = 0.7



def main(args=None):
    rclpy.init(args=args)

    navigation = Navigation()

    rclpy.spin(navigation)

    navigation.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()