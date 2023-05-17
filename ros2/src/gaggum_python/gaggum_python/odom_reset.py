import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class odomReset(Node):
    def __init__(self):
        super().__init__('odom_reset')
    # subscriber-----------------------------------
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

    
    # publisher------------------------------------
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)

    # # timer_callbacksio_client_.socket()->on("auto_move", [this](sio::event& event) {
    #     timer_period = 0.5  # seconds
    #     self.timer = self.create_timer(timer_period, self.timer_callback)
        
    # callback 상태 확인용 ---------------------------
        self.is_odom = True        # Odometry


    # 메시지-----------------------------------------
        # self.odom_msg = Odometry()      # odom



    def odom_callback(self, msg):
        if self.is_odom:
            print("callback start!!!!!!!")
            msg.pose.pose.position.x = 0.0
            msg.pose.pose.position.y = 0.0
            msg.pose.pose.position.z = 0.0
            self.is_odom = False
            self.odom_pub.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)

    odom_reset = odomReset()

    rclpy.spin(odom_reset)

    odom_reset.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()