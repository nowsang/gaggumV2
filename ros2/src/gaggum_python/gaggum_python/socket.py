import rclpy
import socketio

from rclpy.node import Node
from gaggum_msgs.msg import TurtlebotStatus,EnviromentStatus, MapScan
from geometry_msgs.msg import Twist,Point
from math import pi,cos,sin,sqrt,atan2


info = {
    "robot" : {
        "x" : 0,
        "y" : 0,
        "mode" : 0,
    },
    "environment" : {
        "month" : 30,
        "day" : 0,
        "hour" : 9,
        "minute" : 0,
        "temperature" : 10,
        "weather" : "Cloudy"
    }
}

# global 변수 설정, msg로 publish 하여 다른 node에서 조건에 맞게 실행하기 위함
# 기본 값은 0 으로 제어 명령을 보내지 않는 상태가 됨.
global map_scan
map_scan = 0
map_scan_end = 0

# socket 
sio = socketio.Client()

@sio.event
def connect():
    print('connection ROS')        
    
@sio.event
def disconnect():
    print('disconnected ROS from server')
    
@sio.event
def connect_error(data):
    print("connect_error!", data)

@sio.on("run_mapping")
def run_mapping(data):                
    print("run_mapping", data)
    global map_scan, map_scan_end
    
    # FRONT -> ROS로 제어 명령 보냄
    if data == 1:
        map_scan = 1
    
    elif data == 0:
        map_scan_end = True


# 자동급수, 자동 물주기 정보 들어오는 곳
@sio.on("auto_move")
def auto_move(data):
    # 여기에 어떤 정보를 가공해서 보내야 할까?
    print("auto_move", data['mode'])    

    
# ip_server = 'http://localhost:3001'
ip_server = "https://j8b310.p.ssafy.io/socket"


print("connect ", ip_server)
sio.connect(ip_server)



class SocketClass(Node):

    def __init__(self):
        super().__init__('socket_info') 

        # 맵 만들 때 필요한 변수를 저장하는 주소 publish
        self.map_scan_publisher = self.create_publisher(MapScan, '/map_scan', 10)
        # 터틀 봇 맵 작동 정보 구독
        self.map_scan_sub = self.create_subscription(MapScan, '/map_scan', self.map_scan_callback, 1000)
        # 환경 변수
        self.envir_sub = self.create_subscription(EnviromentStatus, '/envir_status', self.env_callback, 1000)
        # 터틀봇 정보
        self.turtle_bot_sub = self.create_subscription(TurtlebotStatus, '/turtlebot_status', self.turtlebot_callback, 1000)

        # 물 주기 소켓 통신 한번만 하기 위한 변수
        self.water_cnt = 0
        self.sunny_cnt = 0

        self.timer_period = 1
        self.timer = self.create_timer(self.timer_period, self.timer_callback)       


    # 시뮬레이터 환경 변수 Back에 전달.
    def env_callback(self, msg):

        info["environment"]["month"] = msg.month
        info["environment"]["day"] = msg.day
        info["environment"]["hour"] = msg.hour
        info["environment"]["minute"] = msg.minute
        info["environment"]["weather"] = msg.weather
        info["environment"]["temperature"] = msg.temperature

    # 터틀봇 현재 위치
    def turtlebot_callback(self, msg):

        info["robot"]["x"] = msg.twist.angular.x
        info["robot"]["y"] = msg.twist.angular.y

    def map_scan_callback(self, msg):
  
        if msg.map_scan == -1:
            print("맵 스캔이 종료되었습니다.")
            global map_scan     
            map_scan = -1

            msg.map_scan = 0
            self.map_scan_publisher.publish(msg)    


    # socket 정보를 저장하거나 다른 곳에 쓸 수 있게 callback
    def timer_callback(self):
        global map_scan, map_scan_end

        # run_mapping을 하기위해 만든 함수. msg를 publish해서 run_mapping, wall_tracking을 할 수 있게 한다.
        # map_scan Topic
        msg = MapScan()
        print("MapOperationList", msg)

        if map_scan_end:
            msg.map_scan = 0
            self.map_scan_publisher.publish(msg)
            map_scan_end = False
            map_scan = 0


                    
        # wall_tracking이 종료 되었으면 map_create는 -1이 됨.
        if map_scan == -1:
            print("맵 스캔이 종료 -> 프론트로 데이터 전달.")
            sio.emit("run_mapping", map_scan)

            # 스캔 종료 후 다시 0으로 대기 상태 하기
            map_scan = 0

        # map_scan 작동 명령을 topic에다가 전달. -> run_mapping, wall_tracking 둘다 실행
        elif map_scan == 1:
            msg.map_scan = 1
            self.map_scan_publisher.publish(msg)

            
        # envir_status 정보를 socket 통신을 통해 백에 전달.
        if info["environment"]["hour"] == 13 and self.water_cnt == 0:
            self.water_cnt = 1
            sio.emit("simulator_info", info)

        elif info["environment"]["hour"] == 15 and self.sunny_cnt == 0:
            self.sunny_cnt = 1
            sio.emit("simulator_info", info)


        

def main(args=None):
        
    rclpy.init(args=args)    
    

    socket_info = SocketClass()
    rclpy.spin(socket_info)   
    socket_info.destory_node() 
    rclpy.shutdown()


if __name__ == '__main__':
    main()
