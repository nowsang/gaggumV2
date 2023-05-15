import numpy as np
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import os

class IMGParser(Node):

    def __init__(self):
        super().__init__(node_name='pytorch_detector')
        self.subscription_img = self.create_subscription(CompressedImage, 'camera/image_raw/compressed', self.img_callback, 10)
        self.img_bgr = None
        self.timer_period = 0.1
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.img_counter = 601
        
    def img_callback(self, msg):
        np_arr = np.frombuffer(msg.data, np.uint8)
        self.img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        self.resized_img = cv2.resize(self.img_bgr, (640, 480))

    def yolov5_detect(self, img_bgr):
        cv2.imshow("show and write image", img_bgr)
        key = cv2.waitKey(1) & 0xFF

        save_directory = 'plants_gaggum'

        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        if key == ord('z'):
            img_name = f'plants_{self.img_counter}.jpg'
            img_path = os.path.join(save_directory, img_name)
            cv2.imwrite(img_path, img_bgr)
            print(f'Image saved as {img_path}')
            self.img_counter += 1

    def timer_callback(self):
        if self.img_bgr is not None:
            self.yolov5_detect(self.resized_img)
        else:
            pass

def main(args=None):

    rclpy.init(args=args)

    image_parser = IMGParser()

    rclpy.spin(image_parser)

    image_parser.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':

    main()