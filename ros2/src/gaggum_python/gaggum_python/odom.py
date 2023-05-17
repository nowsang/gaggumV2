import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose, Point, Quaternion
from nav_msgs.msg import Odometry

class OdomInitializer(Node):
    def __init__(self):
        super().__init__('odom_initializer')
        self.publisher = self.create_publisher(Odometry, 'odom', 10)
        
        # Initialize the odometry message
        self.odom = Odometry()
        self.odom.header.frame_id = 'odom'
        self.odom.child_frame_id = 'base_link'
        
        self.odom.pose.pose = Pose()
        self.odom.pose.pose.position = Point()
        self.odom.pose.pose.orientation = Quaternion()
        
        # Set the initial values
        self.odom.pose.pose.position.x = 0.0
        self.odom.pose.pose.position.y = 0.0
        self.odom.pose.pose.position.z = 0.0
        
        self.odom.pose.pose.orientation.x = 0.0
        self.odom.pose.pose.orientation.y = 0.0
        self.odom.pose.pose.orientation.z = 0.0
        self.odom.pose.pose.orientation.w = 1.0
        
        self.publish_odom()
    
    def publish_odom(self):
        self.odom.header.stamp = self.get_clock().now().to_msg()
        self.publisher.publish(self.odom)
        print('초기화')
    
def main(args=None):
    rclpy.init(args=args)
    odom_initializer = OdomInitializer()
    
    rclpy.spin(odom_initializer)
    
    odom_initializer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
