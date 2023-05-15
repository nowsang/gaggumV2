import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry

class handControl(Node):
    def __init__(self):
        super().__init__('hand_control')
    # subscriber-----------------------------------
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
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

    def timer_callback(self):
        pass

    # callback 함수 ------------------------
    def odom_callback(self, msg):
        self.is_odom = True
        self.odom_msg = msg

    def twist_callback(self, msg):
        self.is_twist = True
        self.twist_msg = msg

def main(args=None):
    rclpy.init(args=args)

    hand_control = handControl()

    rclpy.spin(hand_control)

    hand_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()