# import torch
# import numpy as np
# import cv2
# import os
# import math
# import rclpy
# import time
# import base64

# from rclpy.node import Node

# from sensor_msgs.msg import CompressedImage, LaserScan, Imu
# from geometry_msgs.msg import Twist
# from ssafy_msgs.msg import TurtlebotStatus, Detection

# from squaternion import Quaternion


# class detection_net_class():
#     def __init__(self):
#         # yolo v5
#         os_file_path = os.path.abspath(__file__)
#         full_path = os_file_path.replace('install\\gaggum\\Lib\\site-packages\\gaggum\\yolov5.py', 
#                                         'ros2_smart_home\\gaggum\\gaggum\\model_weights\\gaggum_weight_final.pt')
#         # remote_yolov5_path = "ultralytics/yolov5"
#         local_yolov5_path = os_file_path.replace('install\\gaggum\\Lib\\site-packages\\gaggum\\yolov5.py', 'yolov5')
        
#         self.model = torch.hub.load(local_yolov5_path, 'custom', path=full_path, source='local', force_reload=True)

#         self.model.conf = 0.75

#     def inference(self, image_np):
        
#         results = self.model(image_np)

#         info = results.pandas().xyxy[0]
#         # print(f"info : {info}")
#         #      xmin    ymin    xmax   ymax  confidence  class    name
#         # 0  749.50   43.50  1148.0  704.5    0.874023      0  plant1
#         # 1  433.50  433.50   517.5  714.5    0.687988      1  plant2
#         # 2  114.75  195.75  1095.0  708.0    0.624512      2  plant3
#         # 3  986.00  304.00  1028.0  420.0    0.286865      3  plant4
#         # 4  986.00  304.00  1028.0  420.0    0.286865      4  plant5
        
#         idx_detect = info.index.to_numpy()
#         boxes_detect = info[info['confidence'] > 0.75][['xmin', 'ymin', 'xmax', 'ymax']].to_numpy()
#         classes_pick = info[['name']].T.to_numpy()
#         info_result = info[info['confidence'] > 0.75].to_numpy()

#         return np.squeeze(results.render()), boxes_detect, classes_pick, info_result

# def visualize_images(image_out):

#     winname = 'Vehicle Detection'
#     cv2.imshow(winname, image_out)
#     cv2.waitKey(1)

# def img_callback(msg):

#     global img_bgr
#     global origin_img
#     global is_img_bgr

#     origin_img = msg.data
#     is_img_bgr = True
#     np_arr = np.frombuffer(msg.data, np.uint8)
#     img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

# def scan_callback(msg):
#     global xyz
#     global is_scan
#     is_scan = True
#     R = np.array(msg.ranges)

#     x = R*np.cos(np.linspace(0, 2*np.pi, 360))
#     y = R*np.sin(np.linspace(0, 2*np.pi, 360))
#     z = np.zeros_like(x)

#     xyz = np.concatenate([
#         x.reshape([-1, 1]),
#         y.reshape([-1, 1]),
#         z.reshape([-1, 1])
#     ], axis=1)
#     is_scan = True

# def imu_callback(msg):
#     global is_imu
#     is_imu =True
#     '''
#     로직 3. IMU 에서 받은 quaternion을 euler angle로 변환해서 사용(라디안 단위)
#     각도(도) = 라디안 * 180/π
#     '''
#     global robot_yaw
#     imu_q= Quaternion(msg.orientation.w,msg.orientation.x,msg.orientation.y,msg.orientation.z)
#     _,_,robot_yaw = imu_q.to_euler()
#     # print(f"robot_yaw : {robot_yaw}")

# def status_callback(msg):
#     global turtlebot_status_msg
#     global loc_x,loc_y,loc_z
#     global is_status
#     is_status = True
#     loc_x = msg.twist.angular.x
#     loc_y = msg.twist.angular.y
#     loc_z = 0.0

#     turtlebot_status_msg = msg

# # lidar 좌표계를 bot에서의 좌표계로 변환하는 matrix
# def transformMTX_lidar2bot(params_lidar, params_bot):
#     global loc_x
#     global loc_y
#     global loc_z

#     lidar_yaw, lidar_pitch, lidar_roll = np.deg2rad(params_lidar["YAW"]), np.deg2rad(params_lidar["PITCH"]), np.deg2rad(params_lidar["ROLL"])
#     bot_yaw, bot_pitch, bot_roll = np.deg2rad(params_bot["YAW"]), np.deg2rad(params_bot["PITCH"]), np.deg2rad(params_bot["ROLL"])
    
#     lidar_pos = [params_lidar["X"], params_lidar["Y"], params_lidar["Z"]]
#     bot_pos = [params_bot["X"], params_bot["Y"], params_bot["Z"]]
 
#     Tmtx = translationMtx(lidar_pos[0] - bot_pos[0], lidar_pos[1] - bot_pos[1], lidar_pos[2] - bot_pos[2])
#     Rmtx = rotationMtx(0, 0, 0)

#     RT = np.matmul(Rmtx, Tmtx)

#     return RT

# # bot 좌표계를 global(map)에서의 좌표계로 변환하는 matrix
# def transformMTX_bot2map():
#     global robot_yaw
#     global loc_x
#     global loc_y
#     global loc_z

#     bot_yaw, bot_pitch, bot_roll = np.deg2rad(robot_yaw), np.deg2rad(0.0), np.deg2rad(0.0)
#     map_yaw, map_pitch, map_roll = np.deg2rad(0.0), np.deg2rad(0.0), np.deg2rad(0.0)
    
#     bot_pos = [loc_x, loc_y, loc_z]
#     map_pos = [0.0, 0.0, 0.0]

#     Tmtx = translationMtx(bot_pos[0] - map_pos[0], bot_pos[1] - map_pos[1], bot_pos[2] - map_pos[2])
#     Rmtx = rotationMtx(bot_yaw, bot_pitch, bot_roll)

#     RT = np.matmul(Rmtx, Tmtx)

#     return RT

# # lidar 좌표계를 bot에서의 좌표계로 변환함수
# def transform_lidar2bot(xyz_p):
#     """
#     로직. RT_Lidar2Bot로 라이다 포인트들을 터틀봇 좌표계로 변환시킨다.
#     """
#     global RT_Lidar2Bot

#     xyz_p = np.matmul(xyz_p, RT_Lidar2Bot.T)
    
#     return xyz_p

# # bot 좌표계를 map(global)에서의 좌표계로 변환함수
# def transform_bot2map(xyz_p):
#     """
#     로직. RT_Bot2Map로 터틀봇에서의 좌표들을 글로벌 좌표계로 변환시킨다.
#     """
#     global RT_Bot2Map

#     xyz_p = np.matmul(xyz_p, RT_Bot2Map.T)
    
#     return xyz_p

# def main(args=None):
    
#     yolov5 = detection_net_class()

#     global g_node
#     global turtlebot_status_msg
#     global origin_img

#     global is_img_bgr
#     global is_scan
#     global is_imu
#     global is_status

#     is_img_bgr = False
#     is_scan = False
#     is_imu = False
#     is_status = False

#     global loc_x
#     global loc_y
#     global loc_z

#     rclpy.init(args=args)
#     g_node = rclpy.create_node('tf_detector')

#     subscription_turtle = g_node.create_subscription(TurtlebotStatus, '/turtlebot_status',status_callback, 10)
#     subscription_img = g_node.create_subscription(CompressedImage, '/image_jpeg/compressed', img_callback, 3)
#     subscription_scan = g_node.create_subscription(LaserScan, '/scan', scan_callback, 3)
#     subscription_imu = g_node.create_subscription(Imu,'/imu',imu_callback,10)
#     publisher_detect = g_node.create_publisher(Detection, "/yolo_detected", 10)
    

#     turtlebot_status_msg = TurtlebotStatus()
    
#     l2c_trans = LIDAR2CAMTransform(params_cam, params_lidar)

#     global RT_Lidar2Bot
#     global RT_Bot2Map

#     while rclpy.ok():

#         time.sleep(0.05)
        
#         for _ in range(2):
#             rclpy.spin_once(g_node)

#         detections = Detection()
#         if is_img_bgr and is_scan and is_status and is_imu:
#             image_process, boxes_detect, classes_pick, info_result = yolov5.inference(img_bgr)
#             print("--------------------new_frame--------------------")
#             loc_z = 0
#             loc_z = 0.0

#             xyz_p = xyz[np.where(xyz[:, 0]>=0)]

#             xyz_c = l2c_trans.transform_lidar2cam(xyz_p)

#             xy_i = l2c_trans.project_pts2img(xyz_c, False)

#             xyii = np.concatenate([xy_i, xyz_p], axis=1)

#             RT_Lidar2Bot = transformMTX_lidar2bot(params_lidar, params_bot)
#             RT_Bot2Map = transformMTX_bot2map()

#             # 로직 12. bounding box 결과 좌표 뽑기(num, x, y, distance, cx, cy, object_class)
#             if len(info_result) == 0:
#                 detections.num_index = 0
#                 detections.x = []
#                 detections.y = []
#                 detections.distance = []
#                 detections.cx = []
#                 detections.cy = []
#                 detections.object_class = []
#                 publisher_detect.publish(detections)
#             else :
#                 boxes_all = []
#                 for boxes in boxes_detect:
#                     boxes_np = np.array(boxes)
#                     x = boxes_np.T[0]
#                     y = boxes_np.T[1]
#                     w = (boxes_np.T[2] - boxes_np.T[0])
#                     h = (boxes_np.T[3] - boxes_np.T[1])

#                     bbox = np.vstack([
#                         x.astype(np.int32).tolist(),
#                         y.astype(np.int32).tolist(),
#                         w.astype(np.int32).tolist(),
#                         h.astype(np.int32).tolist()
#                     ]).T

#                     boxes_all.append(bbox)
#                 boxes_all = np.array(boxes_all)

#                 ostate_list = []
#                 angles = []
#                 for k, bbox in enumerate(boxes_all):
#                     for i in range(bbox.shape[0]):
#                         x = int(bbox[i, 0])
#                         y = int(bbox[i, 1])
#                         w = int(bbox[i, 2])
#                         h = int(bbox[i, 3])

#                         cx = int(x + (w / 2))
#                         cy = int(y + (h / 2))

#                         xyv = xyii[np.logical_and(xyii[:, 0]>=cx-(w/2 * 0.7), xyii[:, 0]<=cx+(w/2 * 0.7)), :]
#                         xyv = xyv[np.logical_and(xyv[:, 1]>=y, xyv[:, 1]<=y+h), :]

#                         ostate = np.median(xyv, axis=0)
                        
#                         relative_x = ostate[2]
#                         relative_y = ostate[3]
#                         relative_z = ostate[4]

#                         relative = np.array([relative_x, relative_y, relative_z, 1])

#                         object_global_pose = transform_bot2map(transform_lidar2bot(relative))

#                         x2 = loc_x + relative_x * math.cos(robot_yaw)
#                         y2 = loc_y + relative_x * math.sin(robot_yaw)
#                         angles.append(robot_yaw * 180.0 / math.pi)

#                         ostate_list.append(object_global_pose)

#                         detections.num_index = len(info_result)
#                         detections.x.append(x2)
#                         detections.y.append(y2)
#                         detections.distance.append(relative_x)
#                         detections.cx.append(cx)
#                         detections.cy.append(cy)
#                         detections.object_class.append(info_result[k][5])

#                 publisher_detect.publish(detections)

#             for i in range(detections.num_index):
#                 print("idx : {}, object_class : {}, xy : ({}, {}), distance : {}, cxy : ({}, {}), angles : {}"
#                       .format(i, detections.object_class[i], detections.x[i], detections.y[i], 
#                               detections.distance[i], detections.cx[i], detections.cy[i], angles[i]))
                
#             image_process = draw_pts_img(image_process, xy_i[:, 0].astype(np.int32), xy_i[:, 1].astype(np.int32))

#             visualize_images(image_process)

#     g_node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':

#     main()
