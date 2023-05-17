from rclpy.qos import qos_profile_sensor_data, QoSProfile
from sensor_msgs.msg import LaserScan
import rclpy

def chatter_callback(msg):
    print(msg)

def main():
    
    rclpy.init()
    qos = QoSProfile(depth=10)
    node = rclpy.create_node('scan_listener')
    sub = node.create_subscription(LaserScan,'scan',chatter_callback, qos_profile=qos_profile_sensor_data)
    try:
        while True:
            rclpy.spin_once(node)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    print('Starting scan listener')
    main()
    print('done.') 