import rclpy
import cv2
import socketio
import base64

from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist, Point, Point32, Pose, PoseStamped
from gaggum_msgs.msg import Detection
from squaternion import Quaternion
from nav_msgs.msg import Odometry,Path
from math import pi,cos,sin,sqrt,atan2, pow
import numpy as np
from sensor_msgs.msg import LaserScan, PointCloud
from std_msgs.msg import Int16

# path_tracking 노드는 로봇의 위치(/odom), 로봇의 속도(/turtlebot_status), 주행 경로(/local_path)를 받아서, 주어진 경로를 따라가게 하는 제어 입력값(/cmd_vel)을 계산합니다.
# 제어입력값은 선속도와 각속도로 두가지를 구합니다. 


# 노드 로직 순서
# 1. 제어 주기 및 타이머 설정
# 2. 파라미터 설정
# 3. Quaternion 을 euler angle 로 변환
# 4. 터틀봇이 주어진 경로점과 떨어진 거리(lateral_error)와 터틀봇의 선속도를 이용해 전방주시거리 계산
# 5. 전방 주시 포인트 설정
# 6. 전방 주시 포인트와 로봇 헤딩과의 각도 계산
# 7. 선속도, 각속도 정하기

global auto_mode_info, is_trigger

auto_mode_info = False
is_trigger = False
diary_regist_li = []
diary_regist = {
    'plant_original_name' : 'None',
    'plant_img' : 'None',
}

# # socket 
# sio = socketio.Client()

# @sio.event
# def connect():
#     print('connection ROS')        
    
# @sio.event
# def disconnect():
#     print('disconnected ROS from server')
    
# @sio.event
# def connect_error(data):
#     print("connect_error!", data)

# # 자동급수, 자동 물주기 정보 들어오는 곳
# @sio.on("auto_move")
# def auto_move(data):    
#     global auto_mode_info, is_trigger

#     # 소켓에서 들어오는 자동 급수 식물 정보
#     auto_mode_info = data

#     # 자동 급수 하기위해 필요한 변수
#     is_trigger = True

#     for plant in data['data']:
#         print(plant['plant_name'])

# ip_server = "https://j8b310.p.ssafy.io/socket"
# # ip_server = 'http://localhost:3001'

# print("connect ", ip_server)
# sio.connect(ip_server)

class followTheCarrot(Node):
    def __init__(self):
        super().__init__('path_tracking') 

        # 로봇을 움직이게 하는 부분
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        # 로봇의 현재 위치
        self.subscription = self.create_subscription(Odometry,'/odom',self.odom_callback,10)
        self.status_sub = self.create_subscription(Twist,'/cmd_vel',self.status_callback,10)

        # 경로 받아오기
        self.path_sub = self.create_subscription(Path,'/local_path',self.path_callback,10)

        # 라이다 데이터 구독
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)

        # 로직 1. 제어 주기 및 타이머 설정
        time_period=0.05
        self.timer = self.create_timer(time_period, self.timer_callback)

        # handcontrol node에 제어 메시지를 보냄
        self.hand_control_pub = self.create_publisher(Int16, '/hand_control_cmd', 10)

        # 목표 좌표를 가지고 옴
        # self.goal_sub = self.create_subscription(PoseStamped,'/goal_pose',self.goal_callback, 1)

        # a_star에 목표 좌표를 보냄
        self.a_star_goal_pub = self.create_publisher(Point, '/a_star_goal', 10)

        # yolo에서 정보를 받아옴
        self.yolo_sub = self.create_subscription(Detection, '/yolo_detected', self.yolo_callback, 10)

        # 카메라에서 이미지 정보를 받아옴
        self.subs_img = self.create_subscription(CompressedImage, '/image_jpeg/compressed', self.img_callback, 1)


        self.is_odom = False
        self.is_path = False
        self.is_status = False
        self.is_forward_approach = False
        self.is_right_approach = False
        self.is_left_approach = False
        self.is_trigger = True
        self.is_yolo = False
        self.is_pointed = False

        self.odom_msg=Odometry()            
        self.robot_yaw=0.0
        self.turtle_yaw = 0.0
        self.path_msg=Path()
        self.cmd_msg=Twist()

        self.handcontrol_cmd_msg = Int16()

        # 로직 2. 파라미터 설정(전방주시거리)
        self.lfd=0.1
        self.min_lfd=0.1
        self.max_lfd=1.0

        # 터틀봇이 정지해있는지 판단
        self.stop_cnt = 0 # 터틀봇이 멈춰 있는지 판단하는 간격을 정하기 위한 변수
        self.is_stop = False # 터틀봇의 정지 여부 판단
        self.out_vel = 0.0 # 탈출을 계속하기 위해 필요함
        self.out_rad_vel = 0.0

        self.turn_cnt = 0
        self.go_cnt = 0
        self.back_cnt = 0

        # 라이다 주변 접근 정보
        self.forward_dis = 0
        self.left_dis = 0
        self.right_dis = 0

         # 터틀봇의 현재 위치
        self.robot_pose_x = 0
        self.robot_pose_y = 0

        # 백에서 넘어오는 trigger
        self.triggers = {
            'data': [
                {'plant_number': 3, 'plant_original_name': 'plant3', 'plant_position_x': 1.5023, 'plant_position_y': 0.9781},
            ], 
            'mode': 100  
        #     'data': [
        #         {'plant_number': 1, 'plant_original_name': 'plant1', 'plant_position_x': -4.87, 'plant_position_y': 3.48},
        #         {'plant_number': 2, 'plant_original_name': 'plant2', 'plant_position_x': -2.92, 'plant_position_y': 3.49}
        #     ],
        #     'mode': 200,
        #     'sunSpots': [
        #         {'sunspot_number': 0, 'sunspot_isplant': 0, 'sunspot_x_position': 0, 'sunspot_y_position': 0},
        #         {'sunspot_number': 2, 'sunspot_isplant': 0, 'sunspot_x_position': -1.99, 'sunspot_y_position': 4.53},
        #         {'sunspot_number': 3, 'sunspot_isplant': 0, 'sunspot_x_position': -2.24, 'sunspot_y_position': 6.01},
        #         {'sunspot_number': 4, 'sunspot_isplant': 0, 'sunspot_x_position': -2.11, 'sunspot_y_position': 9.34},
        #         {'sunspot_number': 5, 'sunspot_isplant': 0, 'sunspot_x_position': -2.07, 'sunspot_y_position': 10.1}
        #     ]
        }
        
        # trigger 정보
        self.goal_x = 0
        self.goal_y = 0
        self.plant_original_name = ''
        self.palnt_number = 0
        self.triggers_idx = 0   # 현위치에서 가까운 화분의 인덱스
        self.visited = set()
        self.sun_spot_x = 0
        self.sun_spot_y = 0
       
       # yolo에서 받아온 정보
        self.yolo_msg = Detection()
        self.yolo_distance = 0
        self.yolo_number = 0
        self.yolo_cx = 0
        self.yolo_cy = 0

        # 카메라 센서 이미지
        self.original_img = None

        # 물주기 기능에 사용되는 변수
        self.pickture = set()   # 사진은 한번만
        self.water_time = 0     # 물 주는 동안 기다림
        self.check_stop = 0     # 멈췄는 지 확인 하는 함수
        self.is_yolo_finish = False  # 물주기 끝내는 변수

        # 화분 이동 기능에 사용되는 변수
        self.hand_control_msg = Int16() # handcontrol에 모드를 보냄       
        self.is_lift = False    # 화분을 들고 있는 지 확인
        self.lift_time = 0
        self.lift_idx = 0
        self.is_close = False
        self.is_put_wait = False

        # 물 주기 완료 후 백으로 다시 전달하는 변수
        self.diary_regist = {
            'plant_original_name' : 'None',
            'plant_img' : 'None',
        }   

    def timer_callback(self):
        print("이거 받아 왔니>???", self.is_status)
        # 백에서 트리거가 실행되면 소켓을 통해 준 정보를 전역변수에 저장한다.        
        global auto_mode_info, is_trigger
        self.triggers = auto_mode_info  
        self.is_trigger = is_trigger          
        
        # 백에서 트리거가 실행되면
        if self.is_trigger:
            self.mode = self.triggers['mode']
            if not self.is_lift:
                # 모든 화분을 갔다면
                if len(self.visited) == len(self.triggers['data']):
                    self.goal_x = -5.818
                    self.goal_y = 6.398
                    # self.is_finish = True
                    self.is_yolo_finish = True

                    if -6.0 <= self.robot_pose_x <= -5.7 and 6.2 <= self.robot_pose_y <= 6.5:
                        self.visited = set()                        
                        self.is_trigger = False
                        is_trigger = False
                        self.is_yolo_finish = False

                        if self.mode == 100:
                            print("물 종료 되었습니다")
                            # sio.emit("watering_finish", "finish")
                            self.is_yolo_finish = False
                            
                        if self.mode == 200:
                            print("화분 이동 종료")
                            self.is_yolo_finish = False

                        
            
                else:
                    # 가까이에 있는 좌표 찾기
                    x1 = self.robot_pose_x
                    y1 = self.robot_pose_y
                    min_dis = float('inf')
                    for i in range(len(self.triggers['data'])):    
                        x2 = self.triggers['data'][i]['plant_position_x']
                        y2 = self.triggers['data'][i]['plant_position_y']
                        dis = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
                        # print(f'{i}번 거리: {dis}')
                        if dis < min_dis and i not in self.visited:
                            min_dis = dis
                            self.triggers_idx = i
                    # print('self.triggers_idx', self.triggers_idx)
                        self.goal_x = self.triggers['data'][self.triggers_idx]['plant_position_x']
                        self.goal_y = self.triggers['data'][self.triggers_idx]['plant_position_y']
                        self.plant_original_name = self.triggers['data'][self.triggers_idx]['plant_original_name']
                        self.plant_number = self.triggers['data'][self.triggers_idx]['plant_number']
                        self.plant_name = self.triggers['data'][self.triggers_idx]['plant_name']
           
            

            # 로봇의 현재 위치를 나타내는 변수
            self.robot_pose_x = self.odom_msg.pose.pose.position.x
            self.robot_pose_y = self.odom_msg.pose.pose.position.y
            
            # yolo가 넘어오면
            # print('yolo가 넘어오면', self.is_yolo, self.is_yolo_finish, self.is_lift)
            if self.is_yolo and not self.is_yolo_finish and not self.is_lift:
                # print('실행중')
                    # print('is_pointed', self.is_pointed)
                    # 화분 앞에 위치하지 않으면
                    # 
                    
                    if not self.is_pointed:
                        try:
                            idx = self.yolo_msg.object_class.index(self.plant_number - 1)
                            self.yolo_distance = self.yolo_msg.distance[idx]
                            self.yolo_number = self.yolo_msg.object_class[idx]
                            self.yolo_cx = self.yolo_msg.cx[idx]
                            self.yolo_cy = self.yolo_msg.cy[idx]
                            # print(idx, self.yolo_distance, self.yolo_number, self.yolo_cx, self.yolo_cy)
                            
                            # 거리가 1이하이면
                            if self.yolo_distance <= 1:
                                self.cmd_msg.linear.x=0.0
                                self.cmd_msg.angular.z=0.0

                                # 조금이라도 움직이면 멈춤확인 초기화
                                if  self.cmd_msg.linear.x >= 0.05:
                                    self.check_stop=0

                                # print("화분일치 들어가기 전", self.yolo_number, self.plant_number)
                                # 목표 화분인지 확인하고(화분 번호는 백에서는 1번 부터 시작,yolo는 0번 부터 시작)
                                if  self.yolo_number == self.plant_number - 1:   
                                    # print("화분일치?", self.yolo_number, self.plant_number)
                                    self.is_stop = True
                                    # 중앙 맞추기 160
                                    if 150 <= self.yolo_cx <= 170:
                                        # 중간에 있으면 천천히 전진
                                        self.cmd_msg.angular.z=0.0
                                        self.cmd_msg.linear.x=0.1

                                        if self.yolo_distance <= 1:
                                            self.cmd_msg.linear.x=0.1
                                            if 0.5 <= self.yolo_distance <= 0.6:
                                                self.cmd_msg.linear.x=0.0
                                                self.cmd_msg.angular.z=0.0
                                                self.check_stop += 1
                                                print(f'중앙 정렬 진행도 {self.check_stop * 2}%')
                                                if self.check_stop >= 50:
                                                    self.check_stop = 0
                                                    self.is_pointed = True
                                            else:
                                                # 너무 가까우면 후진하기
                                                if self.yolo_distance < 0.55:
                                                    self.cmd_msg.linear.x=-0.1
                                                    self.cmd_msg.angular.z=0.0
                                    # 목표가 왼쪽에 있으면
                                    else:
                                        print('위치 조정 중...')
                                        if self.yolo_cx < 150:
                                            self.cmd_msg.angular.z=-0.05                            

                                        # 목표가 오른쪽에 있으면
                                        else:
                                            self.cmd_msg.angular.z=0.05
                                
                                else:
                                    # 목표 화분이 아니면 회피해서 목표 지점으로 가기
                                    # print('목표 화분 아님')
                                    self.is_stop = False 
                                #print('x', self.cmd_msg.linear.x, 'z', self.cmd_msg.angular.z)
                            
                            # 1미터 밖에 있으면 경로따라 가기
                            else:
                                self.is_stop = False
                        except IndexError:
                            # print('화분 없음')
                            pass
                            
                        except ValueError:
                            # print('1미터 이내 목표 화분이 yolo에 없음')
                            self.is_stop = False
                            # 화분 앞에서 정지한 상태
                    else:
                        # 물 줄때는 사진 찍기
                        if self.mode == 100:
                            if self.plant_number not in self.pickture:
                                print('사진 찍기')
                                photo_msg = Tts()
                                photo_msg.shutter = True
                                self.tts_pub.publish(photo_msg) 
                                self.diary_regist['plant_img'] = self.base64_img
                                self.pickture.add(self.plant_number)

                        # 전방 접근 상태
                        # print(f'접근했니? : {self.is_forward_approach}, {self.forward_dis}')
                        if self.is_forward_approach:
                            self.cmd_msg.linear.x=0.0
                            if self.mode == 100:
                                self.water_time += 1
                                print(f'물 주기 {self.water_time} %')
                                #물 주는 신호 TTS(한번만 실행)
                                water_msg = Tts()
                                if self.water_time == 1:                                        
                                    water_msg.water_mode = True
                                    self.tts_pub.publish(water_msg)
                                # 물 다줬으면 다음 좌표로 이동하기
                                if self.water_time >= 100:
                                    print(f'{self.plant_original_name} 물 주기 완료')
                                    # 물 주기 완료 TTS 실행
                                    water_msg.water_mode_end = True
                                    self.tts_pub.publish(water_msg)
                                    # 물 주는게 완료 되었으면 백에 사진과 화분정보 제공
                                    self.diary_regist['plant_original_name'] = self.plant_original_name
                                    # sio.emit('diary_regist', self.diary_regist)
                                    self.water_time = 0
                                    self.visited.add(self.triggers_idx)
                                    self.is_pointed = False
                                    self.is_stop = False
                            else:
                                print('화분 드는 중')
                                self.lift_time += 1
                                if self.lift_time >= 50:
                                    self.hand_control_msg.data = 2
                                    self.hand_control_pub.publish(self.hand_control_msg)
                                    
                                    self.is_lift = True
                                    self.lift_time = 0
                                    # 들면 a_star로 목적지를 바꿔야 하잖아
                                    for i in range(1, len(self.triggers['sunSpots'])):
                                        # 그 자리에 화분이 없으면
                                        if self.triggers['sunSpots'][i]['sunspot_isplant'] == 0:
                                            self.goal_x = self.triggers['sunSpots'][i]['sunspot_x_position']
                                            self.goal_y = self.triggers['sunSpots'][i]['sunspot_y_position']
                                            self.triggers['sunSpots'][i]['sunspot_isplant'] = 1
                                            break
                                    # print(self.goal_x, self.goal_y)
                                    self.visited.add(self.triggers_idx)
                                    self.is_pointed = False
                                    self.is_stop = False
                                
                        elif self.hand_control_msg.data != 2:
                            print('목표에 접근하는 중...')
                            self.cmd_msg.linear.x=0.1

                    self.cmd_pub.publish(self.cmd_msg)
                    self.hand_control_msg.data = 0

            # 1. turtlebot이 연결되어 있고, odom이 작동하며, 경로가 있을 때, yolo가 작동 중일때, stop이 아닐때
            # print(self.is_status, self.is_odom, self.is_path, self.is_stop)
            if self.is_status and self.is_odom and self.is_path and not self.is_stop:

                # 남은 경로가 1 초과 이면
                # print(self.path_msg.poses)
                if len(self.path_msg.poses)> 1:
                    self.is_look_forward_point = False
                    self.handcontrol_cmd_msg.data = 0

                    # 로봇과 가장 가까운 경로점과의 직선거리
                    lateral_error = sqrt(pow(self.path_msg.poses[0].pose.position.x-self.robot_pose_x,2)+pow(self.path_msg.poses[0].pose.position.y-self.robot_pose_y,2))
                    # #print(self.robot_pose_x,self.robot_pose_y,lateral_error)

                    # 로직 4. 로봇이 주어진 경로점과 떨어진 거리(lateral_error)와 로봇의 선속도를 이용해 전방주시거리 설정

                    self.lfd = (self.status_msg.twist.linear.x + lateral_error) * 0.7

                    # 최대, 최소 전방주시거리 제한 (0.1 ~ 1.0m)
                    if self.lfd < self.min_lfd :
                        self.lfd=self.min_lfd
                    if self.lfd > self.max_lfd:
                        self.lfd=self.max_lfd

                    min_dis=float('inf')

                    # 로직 5. 전방 주시 포인트 설정(lfd만큼 떨어진 경로점을 찾는 부분)
                    for num, waypoint in enumerate(self.path_msg.poses):
                        self.current_point = waypoint.pose.position
                        # 로봇과 가장 가까운 경로점과 모든 경로점과의 거리 탐색
                        dis = sqrt(pow(self.path_msg.poses[0].pose.position.x - self.current_point.x, 2) + pow(self.path_msg.poses[0].pose.position.y - self.current_point.y, 2))
                        if abs(dis-self.lfd) < min_dis:
                            min_dis = abs(dis-self.lfd)
                            # 경로점을 넣어준다
                            self.forward_point = self.current_point
                            self.is_look_forward_point = True
                            target_num = num

                    if self.is_look_forward_point: 
                        # 전방 주시 포인트
                        global_forward_point=[self.forward_point.x, self.forward_point.y, 1]

                        '''
                        로직 6. 전방 주시 포인트와 로봇 헤딩과의 각도 계산
                        (테스트) 맵에서 로봇의 위치(self.robot_pose_x,self.robot_pose_y)가 (5,5)이고, 헤딩(self.robot_yaw) 1.57 rad 일 때, 선택한 전방포인트(global_forward_point)가 (3,7)일 때
                        변환행렬을 구해서 전방포인트를 로봇 기준좌표계로 변환을 하면 local_forward_point가 구해지고, atan2를 이용해 선택한 점과의 각도를 구하면
                        theta는 0.7853 rad 이 나옵니다.
                        trans_matrix는 로봇좌표계에서 기준좌표계(Map)로 좌표변환을 하기위한 변환 행렬입니다.
                        det_tran_matrix는 trans_matrix의 역행렬로, 기준좌표계(Map)에서 로봇좌표계로 좌표변환을 하기위한 변환 행렬입니다.  
                        local_forward_point 는 global_forward_point를 로봇좌표계로 옮겨온 결과를 저장하는 변수입니다.
                        theta는 로봇과 전방 주시 포인트와의 각도입니다. 
                        '''
                        trans_matrix = np.array([       
                                                [cos(self.robot_yaw), -sin(self.robot_yaw), self.robot_pose_x],
                                                [sin(self.robot_yaw), cos(self.robot_yaw), self.robot_pose_y],
                                                [0, 0, 1],
                        ])
                        # 역행렬 만들기
                        det_trans_matrix = np.linalg.inv(trans_matrix)
                        # 글로벌 경로를 역행렬 연산 => 로컬 경로를 알아냄   
                        local_forward_point = det_trans_matrix.dot(global_forward_point)
                        # 로봇과 전방주시 포인트간의 차이값 계산
                        theta = -atan2(local_forward_point[1], local_forward_point[0])
                        
                        # 로직 7. 선속도, 각속도 정하기
                        out_vel = 0.5
                        out_rad_vel = theta
                        # 10이내의 거리에서 선속도를 줄이고 각속도를 높여서 목표 지점을 지나치지 않도록 함
                        if len(self.path_msg.poses) < 20:
                            out_vel = 0.3
                            # 5 이내의 거리에서는 정밀한 제어를 위해 완전히 속도를 줄임
                            if len(self.path_msg.poses) < 10:
                                out_vel = 0.1
                            out_rad_vel = theta
            
                        self.cmd_msg.linear.x = out_vel
                        self.cmd_msg.angular.z = out_rad_vel
                else:
                    # 현재 위치가 목표 좌표 1 영역 이내에 들어왔으면
                    if self.goal_x - 1 <= self.robot_pose_x <= self.goal_x + 1 and self.goal_y - 1 <= self.robot_pose_y <= self.goal_y + 1:
                        print('목표 지점에 도착')
                        # 도착 후 멈추기
                        self.cmd_msg.linear.x=0.0
                        self.cmd_msg.angular.z=0.0
                        
                        # 트리거가 안 끝났는데 
                        if not self.is_yolo_finish:
                            # 화분 들고 있으면
                            if self.is_lift:
                                print('화분 내려 놓는 중')
                                print(f'진행률 {self.lift_time * 2 + 2}%')
                                if not (0.997 <= self.odom_msg.pose.pose.orientation.w <= 0.999):
                                    self.cmd_msg.angular.z=0.15
                                else:
                                    self.hand_control_msg.data = 3
                                    self.hand_control_pub.publish(self.hand_control_msg)
                                    self.is_put_wait = True
                            else:
                                # 목표로 왔는데 화분이 없다 그럼 제자리에서 돌기
                                try:
                                    if self.yolo_msg.object_class[0] != self.plant_number - 1:
                                        print('목표 화분이 아니야')
                                        self.cmd_msg.angular.z=0.3
                                except:
                                    print('목표 지점에 왔는데 화분이 없어!!')
                                    self.cmd_msg.angular.z=0.3
                                
                        else:
                            # 목표 좌표를 찾을 수 없으면 초록색 영역(127) 안에 있다는 말 빠져나오기 위해 후진을 해야함
                            #print("no found forward point")
                            self.cmd_msg.linear.x=-0.1
                            self.cmd_msg.angular.z=0.1

                # 놓고 기다리는 상태
                if self.is_put_wait:
                    self.lift_time += 1
                    # 다 기다렸으면
                    if self.lift_time >= 50:
                        self.is_lift = False
                        self.lift_time = 0
                        self.is_put_wait = False
                else:
                    # 전방 장애물 있으면
                    if self.forward_dis <= 0.2:
                        self.cmd_msg.linear.x=-0.1
                        self.cmd_msg.angular.z = 0.0
                
            # a_star에 목표 좌표를 보냄      
            goal = Point()
            goal.x, goal.y = self.goal_x, self.goal_y
            # print(goal)
            self.a_star_goal_pub.publish(goal)  

        else:
            self.cmd_msg.linear.x=0.0
            self.cmd_msg.angular.z=0.0

        # 터틀봇 제어 명령 
        self.cmd_pub.publish(self.cmd_msg)

    def odom_callback(self, msg):
        self.is_odom=True
        self.odom_msg=msg

        # 로직 3. Quaternion 을 euler angle 로 변환
        q = Quaternion(msg.pose.pose.orientation.w, msg.pose.pose.orientation.x, 
                       msg.pose.pose.orientation.y, msg.pose.pose.orientation.z)
        _, _, self.robot_yaw = q.to_euler()


    def path_callback(self, msg):
        self.is_path=True
        self.path_msg=msg


    def status_callback(self,msg):
        self.is_status=True
        self.status_msg=msg

    # 라이다 데이터 수신시 호출되는 콜백함수
    def lidar_callback(self, msg):
        self.is_lidar = True
        self.lidar_msg = msg
        # 경로와 위치를 알고 있어야 하기 때문에 알고 있는지 체크
        if self.is_path == True and self.is_odom == True:
            # 직교좌표계 데이터를 가질 포인트클라우드 생성
            pcd_msg = PointCloud()
            pcd_msg.header.frame_id = 'map'
            # 로컬 to 글로벌 변환 행렬
            pose_x = self.odom_msg.pose.pose.position.x
            pose_y = self.odom_msg.pose.pose.position.y
            theta = self.robot_yaw
            t = np.array([[cos(theta), -sin(theta), pose_x],
                          [sin(theta), cos(theta), pose_y],
                          [0, 0, 1]])
            # 극좌표계를 직교좌표계로 만들기
            for angle, r in enumerate(msg.ranges):
                global_point = Point32()

                if 0.0 < r < 12:
                    # 극좌표계를 로봇 기준(로컬) 직교좌표계로
                    local_x = r * cos(angle * pi / 180)
                    local_y = r * sin(angle * pi / 180)
                    local_point = np.array([[local_x], [local_y], [1]])
                    # 로컬 직교좌표계를 맵 기준(글로벌) 직교좌표계로
                    global_result = t.dot(local_point)
                    global_point.x = global_result[0][0]
                    global_point.y = global_result[1][0]
                    # 포인트 클라우드에 맵 기준 직교좌표계 데이터 추가
                    # 퍼블리시는 하지 않았지만 확인하고 싶으면 pcd_msg를 퍼블리시해서 rviz에서 확인할 것
                    pcd_msg.points.append(global_point)

            # 전/후방, 좌/우측 충돌 감지
            forward_left = self.lidar_msg.ranges[0:1]
            forward_right = self.lidar_msg.ranges[359:360]
            forward = forward_left + forward_right
            backward = self.lidar_msg.ranges[170:191]
            left = self.lidar_msg.ranges[20:31]
            right = self.lidar_msg.ranges[330:341]

            # 평균 거리 계산
            self.forward_dis = sum(forward) / len(forward)
            backward_dis = sum(backward) / len(backward)
            self.left_dis = sum(left) / len(left)
            self.right_dis = sum(right) / len(right)
            # #print('전방', self.forward_dis)
            # #print('후방', backward_dis)
            # #print('좌측', left_dis)       
            # #print('우측', right_dis)

            # 근접 감지
            if self.forward_dis < 0.2:
                self.is_forward_approach = True
                # print('전방 근접')
            else:
                self.is_forward_approach = False 

            if self.left_dis < 0.2:
                self.is_right_approach = True
            else:
                self.is_forward_approach = False
                #print('좌측 근접')

            if self.right_dis < 0.2:
                self.is_left_approach = True
            else:
                self.is_forward_approach = False
                
                #print('우측 근접')
            # elif backward_dis < 0.25:
            #     self.is_approach = False
            #     #print('후방 근접')


    def yolo_callback(self, msg):
        self.is_yolo = True
        self.yolo_msg = msg

    def img_callback(self, msg):
        self.original_img = msg.data
        np_arr = np.frombuffer(self.original_img, np.uint8)
        cv_img = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
        resized_img = cv2.resize(cv_img, (320, 240))
        _, buffer = cv2.imencode('.jpg', resized_img)
        b64data = base64.b64encode(buffer)
        self.base64_img = b64data.decode('utf-8')
            
def main(args=None):
    rclpy.init(args=args)

    path_tracker = followTheCarrot()

    rclpy.spin(path_tracker)


    path_tracker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main() # 선속도와 각속도로 두가지를 구합니다. 