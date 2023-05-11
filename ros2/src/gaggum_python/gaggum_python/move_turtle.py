import numpy as np
import rclpy
import socketio
import cv2
import base64

from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
from squaternion import Quaternion
from gaggum_msgs.msg import Detection, TurtlebotStatus
import threading

sio = socketio.Client()
global m_control_cmd
m_control_cmd = 0

@sio.event
def connect():
    print('connection established move_client')

@sio.event
def disconnect():
    print('disconnected from server')
    
@sio.on('go_straight')
def go_straight(move):    
    global m_control_cmd
    m_control_cmd = move['data']
    print('go_straight')

@sio.on('go_back')
def back(move):
    print(move['data'])
    global m_control_cmd
    m_control_cmd = move['data']
    print('go_back')

@sio.on('go_left')
def turn_right(move):
    global m_control_cmd
    m_control_cmd = move['data']
    print('go_left')

@sio.on('go_right')
def turn_right(move):
    global m_control_cmd
    m_control_cmd = move['data']
    print('go_right')

def get_global_var():
    return m_control_cmd

def reset_global_var():
    global m_control_cmd
    m_control_cmd = 0

class MoveTurtleBot(Node):

    def __init__(self):
        super().__init__('map_client')
        # self.map_publisher = self.create_publisher(Int8MultiArray, 'map_status', 10)
        # self.automap_publisher = self.create_publisher(Int8MultiArray,'map_auto',10)
        # self.subscription = self.create_subscription(Odometry,'/odom',self.odom_callback,10)
        self.subs_img = self.create_subscription(CompressedImage, '/image_jpeg/compressed', self.img_callback, 1)
        self.yolo_sub = self.create_subscription(Detection, '/yolo_detected', self.yolo_callback, 10)
        self.cmd_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cmd_msg=Twist()

        self.original_img = None
        self.is_yolo = False
        self.yolo_msg = False

        self.timer_period = 0.05
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.m_control_interval = 10
        self.m_control_iter = 0

        sio.connect('https://j8b310.p.ssafy.io/socket')
        # sio.connect('http://localhost:3001')


    def odom_callback(self, msg):
        self.is_odom=True
        self.odom_msg=msg
        q=Quaternion(msg.pose.pose.orientation.w,msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z)
        _,_,self.robot_yaw=q.to_euler()
    
    def img_callback(self, msg):
        self.original_img = msg.data
        np_arr = np.frombuffer(self.original_img, np.uint8)
        cv_img = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
        resized_img = cv2.resize(cv_img, (320, 240))
        _, buffer = cv2.imencode('.jpg', resized_img)
        b64data = base64.b64encode(buffer)
        self.base64_img = b64data.decode('utf-8')

    def yolo_callback(self, msg):
        self.is_yolo = True
        self.yolo_msg = msg
    
    def turtlebot_go(self) :
        self.cmd_msg.linear.x=0.15
        self.cmd_msg.angular.z=0.0


    def turtlebot_back(self) :
        self.cmd_msg.linear.x= -0.15
        self.cmd_msg.angular.z=0.0


    def turtlebot_stop(self) :
        self.cmd_msg.linear.x=0.0
        self.cmd_msg.angular.z=0.0


    def turtlebot_cw_rot(self) :
        self.cmd_msg.linear.x=0.0
        self.cmd_msg.angular.z=0.15


    def turtlebot_cww_rot(self) :
        self.cmd_msg.linear.x=0.0
        self.cmd_msg.angular.z=-0.1

    def timer_callback(self):
        if self.original_img is not None:
            
            def stream_image():
                plant_name = ["plant1", "plant2", "plant3", "plant4", "plant5"]
                if self.yolo_msg:
                    if self.yolo_msg.num_index == 0:
                        x = -100
                        y = -100
                        plant = "none"
                    else:
                        x = self.yolo_msg.x[0]
                        y = self.yolo_msg.y[0]
                        plant = plant_name[self.yolo_msg.object_class[0]]
                else:
                    x = -100
                    y = -100
                    plant = "none"
                data = {
                    "plant_img" : self.base64_img,
                    "plant_position_x" : x,
                    "plant_position_y" : y,
                    "plant_original_name" : plant
                }
                sio.emit("streaming_image", data)

            # 별도의 스레드에서 stream_image 함수를 실행합니다.
            streaming_thread = threading.Thread(target=stream_image)
            streaming_thread.start()
        else:
            pass
 
        # 터틀봇 조작관련 
        ctrl_cmd = get_global_var()

        # # turn left
        if ctrl_cmd == 1:     
            self.turtlebot_cww_rot()

        # go straight
        elif ctrl_cmd == 2:          
            self.turtlebot_go()

        # back        
        elif ctrl_cmd == 3:
            self.turtlebot_back()

        # turn right
        elif ctrl_cmd == 4:
            self.turtlebot_cw_rot()
        
        else:
            self.turtlebot_stop()

        self.cmd_publisher.publish(self.cmd_msg)
        
        if ctrl_cmd != 0: 
            self.m_control_iter += 1

        if self.m_control_iter % self.m_control_interval == 0:

            self.m_control_iter = 0

            reset_global_var()
        

def main(args=None):
    
    rclpy.init(args=args)
    map_client = MoveTurtleBot()
    rclpy.spin(map_client)    
    rclpy.shutdown()
    sio.disconnect()


if __name__ == '__main__':
    main()