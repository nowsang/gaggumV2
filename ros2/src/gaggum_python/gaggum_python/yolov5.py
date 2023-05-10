import torch
import numpy as np
import cv2
import os
import math
import rclpy
import time
import base64

from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from gaggum_msgs.msg import Detection
from nav_msgs.msg import Odometry

from squaternion import Quaternion


class detection_net_class():
    def __init__(self):
        # yolo v5
        os_file_path = os.path.abspath(__file__)
        full_path = os_file_path.replace('install\\gaggum_python\\Lib\\site-packages\\gaggum_python\\yolov5.py', 
                                        'src\\gaggum_python\\gaggum_python\\model_weights\\gaggum_weight_final.pt')
        # remote_yolov5_path = "ultralytics/yolov5"
        local_yolov5_path = os_file_path.replace('install\\gaggum_python\\Lib\\site-packages\\gaggum_python\\yolov5.py', 'src\\yolov5')
        
        self.model = torch.hub.load(local_yolov5_path, 'custom', path=full_path, source='local', force_reload=True)

        self.model.conf = 0.75

    def inference(self, image_np):
        
        results = self.model(image_np)

        info = results.pandas().xyxy[0]
        # print(f"info : {info}")
        #      xmin    ymin    xmax   ymax  confidence  class    name
        # 0  749.50   43.50  1148.0  704.5    0.874023      0  plant1
        # 1  433.50  433.50   517.5  714.5    0.687988      1  plant2
        # 2  114.75  195.75  1095.0  708.0    0.624512      2  plant3
        # 3  986.00  304.00  1028.0  420.0    0.286865      3  plant4
        # 4  986.00  304.00  1028.0  420.0    0.286865      4  plant5
        
        idx_detect = info.index.to_numpy()
        boxes_detect = info[info['confidence'] > 0.75][['xmin', 'ymin', 'xmax', 'ymax']].to_numpy()
        classes_pick = info[['name']].T.to_numpy()
        info_result = info[info['confidence'] > 0.75].to_numpy()

        return np.squeeze(results.render()), boxes_detect, classes_pick, info_result

def visualize_images(image_out):

    winname = 'Vehicle Detection'
    cv2.imshow(winname, image_out)
    cv2.waitKey(1)

def img_callback(msg):

    global img_bgr
    global origin_img
    global is_img_bgr

    origin_img = msg.data
    is_img_bgr = True
    np_arr = np.frombuffer(msg.data, np.uint8)
    img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

def odom_callback(msg):
    global odom_msg
    global loc_x,loc_y,loc_z
    global is_odom
    is_status = True

    loc_x = msg.twist.angular.x
    loc_y = msg.twist.angular.y
    loc_z = 0.0
    odom_msg = msg


def main(args=None):
    
    yolov5 = detection_net_class()

    global g_node
    global origin_img

    global is_img_bgr
    global is_odom

    is_img_bgr = False
    is_odom = False

    rclpy.init(args=args)
    g_node = rclpy.create_node('tf_detector')

    subscription_img = g_node.create_subscription(CompressedImage, 'camera/image_raw/compressed', img_callback, 3)
    subscription_odom = g_node.create_subscription(Odometry,'/odom', odom_callback, 10)
    publisher_detect = g_node.create_publisher(Detection, "/yolo_detected", 10)

    while rclpy.ok():

        time.sleep(0.05)
        
        for _ in range(2):
            rclpy.spin_once(g_node)

        detections = Detection()
        if is_img_bgr and is_odom:
            image_process, boxes_detect, classes_pick, info_result = yolov5.inference(img_bgr)
            print("--------------------new_frame--------------------")

            # 로직 12. bounding box 결과 좌표 뽑기(num, x, y, distance, cx, cy, object_class)
            if len(info_result) == 0:
                detections.num_index = 0
                detections.x = []
                detections.y = []
                detections.distance = []
                detections.cx = []
                detections.cy = []
                detections.object_class = []
                publisher_detect.publish(detections)
            else :
                boxes_all = []
                for boxes in boxes_detect:
                    boxes_np = np.array(boxes)
                    x = boxes_np.T[0]
                    y = boxes_np.T[1]
                    w = (boxes_np.T[2] - boxes_np.T[0])
                    h = (boxes_np.T[3] - boxes_np.T[1])

                    bbox = np.vstack([
                        x.astype(np.int32).tolist(),
                        y.astype(np.int32).tolist(),
                        w.astype(np.int32).tolist(),
                        h.astype(np.int32).tolist()
                    ]).T

                    boxes_all.append(bbox)
                boxes_all = np.array(boxes_all)

                angles = []
                for k, bbox in enumerate(boxes_all):
                    for i in range(bbox.shape[0]):
                        x = int(bbox[i, 0])
                        y = int(bbox[i, 1])
                        w = int(bbox[i, 2])
                        h = int(bbox[i, 3])

                        cx = int(x + (w / 2))
                        cy = int(y + (h / 2))

                        # x2 = loc_x + relative_x * math.cos(robot_yaw)
                        # y2 = loc_y + relative_x * math.sin(robot_yaw)
                        angles.append(robot_yaw * 180.0 / math.pi)

                        detections.num_index = len(info_result)
                        detections.x.append(x2)
                        detections.y.append(y2)
                        detections.distance.append(relative_x)
                        detections.cx.append(cx)
                        detections.cy.append(cy)
                        detections.object_class.append(info_result[k][5])

                publisher_detect.publish(detections)

            for i in range(detections.num_index):
                print("idx : {}, object_class : {}, xy : ({}, {}), distance : {}, cxy : ({}, {}), angles : {}"
                      .format(i, detections.object_class[i], detections.x[i], detections.y[i], 
                              detections.distance[i], detections.cx[i], detections.cy[i], angles[i]))
                
            visualize_images(image_process)

    g_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':

    main()
