import numpy as np
import cv2
import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage, LaserScan

params_lidar = {
    "Range" : 90, #min & max range of lidar azimuths
    "CHANNEL" : int(1), #verticla channel of a lidar
    "localIP": "127.0.0.1",
    "localPort": 9094,
    "Block_SIZE": int(1206),
    "X": 0, # meter
    "Y": 0,
    "Z": 0.19,
    "YAW": 0, # deg
    "PITCH": 0,
    "ROLL": 0
}


params_cam = {
    "WIDTH": 320, # image width
    "HEIGHT": 240, # image height
    "FOV": 60, # Field of view
    "localIP": "127.0.0.1",
    "localPort": 1232,
    "Block_SIZE": int(65000),
    "X": 0.07, # meter
    "Y": 0,
    "Z":  0.15,
    "YAW": 0, # deg
    "PITCH": 0.0,
    "ROLL": 0
}


def rotationMtx(yaw, pitch, roll):
    
    R_x = np.array([[1,         0,              0,                0],
                    [0,         math.cos(roll), -math.sin(roll) , 0],
                    [0,         math.sin(roll), math.cos(roll)  , 0],
                    [0,         0,              0,               1],
                    ])
                     
    R_y = np.array([[math.cos(pitch),    0,      math.sin(pitch) , 0],
                    [0,                  1,      0               , 0],
                    [-math.sin(pitch),   0,      math.cos(pitch) , 0],
                    [0,         0,              0,               1],
                    ])
    
    R_z = np.array([[math.cos(yaw),    -math.sin(yaw),    0,    0],
                    [math.sin(yaw),    math.cos(yaw),     0,    0],
                    [0,                0,                 1,    0],
                    [0,         0,              0,               1],
                    ])
                     
    R = np.matmul(R_x, np.matmul(R_y, R_z))
 
    return R


def translationMtx(x, y, z):
     
    M = np.array([[1,         0,              0,               x],
                  [0,         1,              0,               y],
                  [0,         0,              1,               z],
                  [0,         0,              0,               1],
                  ])
    
    return M


def transformMTX_lidar2cam(params_lidar, params_cam):
    '''
    transform the coordinate of the lidar points to the camera coordinate
    \n xs, ys, zs : xyz components of lidar points w.r.t a lidar coordinate
    \n params_lidar : parameters from lidars 
    \n params_cam : parameters from cameras 
    '''
    lidar_yaw, lidar_pitch, lidar_roll = [np.deg2rad(params_lidar.get(i)) for i in (["YAW","PITCH","ROLL"])]
    cam_yaw, cam_pitch, cam_roll = [np.deg2rad(params_cam.get(i)) for i in (["YAW","PITCH","ROLL"])]
    
    #Relative position of lidar w.r.t cam
    lidar_pos = [params_lidar.get(i) for i in (["X","Y","Z"])]
    cam_pos = [params_cam.get(i) for i in (["X","Y","Z"])]

    x_rel = cam_pos[0] - lidar_pos[0]
    y_rel = cam_pos[1] - lidar_pos[1]
    z_rel = cam_pos[2] - lidar_pos[2]

    R_T = np.matmul(rotationMtx(lidar_yaw, lidar_pitch, lidar_roll).T, translationMtx(-x_rel, -y_rel, -z_rel).T)
    R_T = np.matmul(R_T, rotationMtx(cam_yaw, cam_pitch, cam_roll))
    R_T = np.matmul(R_T, rotationMtx(np.deg2rad(-90.), 0., 0.))
    R_T = np.matmul(R_T, rotationMtx(0, 0., np.deg2rad(-90.)))
    
    #rotate and translate the coordinate of a lidar
    R_T = R_T.T 
    

    return R_T


def make_distance_img(xi, yi, distance, img_w, img_h, dis_max, clr_map):
    '''
    place the lidar points into numpy arrays in order to make distance map
    \n xi, yi : xy components of lidar points w.r.t a 2d normalized plane
    \n distance : distance measurement from the origin of the lidar coordinate
    \n img_w, img_h : a width and a height of a image from a camera
    \n dis_max : maximum of distance shown in the distance map 
    \n clr_map : colormap
    '''
    point_np = np.zeros((img_h,img_w,1), dtype=np.uint8)
    point_binary = np.zeros((img_h,img_w,3), dtype=np.uint8)

    point_np[yi.astype(np.int), xi.astype(np.int), :] = (np.clip(distance,0,dis_max).reshape([-1,1,1])/(dis_max)*255).astype(np.uint8)
    point_binary[yi.astype(np.int), xi.astype(np.int), :] = 1

    point_np = cv2.applyColorMap(point_np, clr_map)

    point_np = cv2.dilate(point_np*point_binary, cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5)))

    return point_np

def make_intensity_img(xi, yi, intens, img_w, img_h):
    '''
    place the lidar points into numpy arrays in order to make intensity map
    \n xi, yi : xy components of lidar points w.r.t a 2d normalized plane
    \n intens : intensities of lidar points
    \n img_w, img_h : a width and a height of a image from a camera
    '''
    point_np = np.zeros((img_h, img_w, 3), dtype=np.uint8)

    #Object
    point_np[yi[intens>=250].astype(np.int),xi[intens>=250].astype(np.int),2] = 255
    
    return point_np

def project2img_mtx(params_cam):
    
    '''
    project the lidar points to 2d plane
    \n xc, yc, zc : xyz components of lidar points w.r.t a camera coordinate
    \n params_cam : parameters from cameras 
    '''
    # focal lengths
    fc_x = params_cam["HEIGHT"]/(2*np.tan(np.deg2rad(params_cam["FOV"]/2)))
    fc_y = params_cam["HEIGHT"]/(2*np.tan(np.deg2rad(params_cam["FOV"]/2)))

    #the center of image
    cx = params_cam["WIDTH"]/2
    cy = params_cam["HEIGHT"]/2
    
    #transformation matrix from 3D to 2D
    R_f = np.array([[fc_x,  0,      cx],
                    [0,     fc_y,   cy]])

    return R_f


class LIDAR2CAMTransform:
    def __init__(self, params_cam, params_lidar):

        self.width = params_cam["WIDTH"]
        self.height = params_cam["HEIGHT"]

        self.n = float(params_cam["WIDTH"])
        self.m = float(params_cam["HEIGHT"])

        self.RT = transformMTX_lidar2cam(params_lidar, params_cam)

        self.proj_mtx = project2img_mtx(params_cam)

    def transform_lidar2cam(self, xyz_p):
        
        xyz_c = np.matmul(np.concatenate([xyz_p, np.ones((xyz_p.shape[0], 1))], axis=1), self.RT.T)

        return xyz_c

    def project_pts2img(self, xyz_c, crop=True):

        xyz_c = xyz_c.T

        xc, yc, zc = xyz_c[0,:].reshape([1,-1]), xyz_c[1,:].reshape([1,-1]), xyz_c[2,:].reshape([1,-1])

        xn, yn = xc/(zc+0.0001), yc/(zc+0.0001)

        xyi = np.matmul(self.proj_mtx, np.concatenate([xn, yn, np.ones_like(xn)], axis=0))

        xyi = xyi[0:2,:].T

        if crop:
            xyi = self.crop_pts(xyi)
        else:
            pass
        
        return xyi

    def crop_pts(self, xyi):

        xyi = xyi[np.logical_and(xyi[:, 0]>=0, xyi[:, 0]<self.width), :]
        xyi = xyi[np.logical_and(xyi[:, 1]>=0, xyi[:, 1]<self.height), :]

        return xyi

    
def draw_pts_img(img, xi, yi):
    '''
    place the lidar points into numpy arrays in order to make intensity map
    \n img : source image
    \n xi, yi : point pixel 
    '''
    point_np = img

    #Left Lane
    for ctr in zip(xi, yi):
        point_np = cv2.circle(point_np, ctr, 2, (255,0,0),-1)

    return point_np


class SensorCalib(Node):

    def __init__(self):
        super().__init__(node_name='ex_calib')

        self.subs_scan = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback, 10)

        self.subs_img = self.create_subscription(
            CompressedImage,
            '/image_jpeg/compressed',
            self.img_callback,
            10)

        self.l2c_trans = LIDAR2CAMTransform(params_cam, params_lidar)

        self.timer_period = 0.1

        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.xyz, self.R, self.intens = None, None, None
        self.img = None

    def img_callback(self, msg):

        np_arr = np.frombuffer(msg.data, np.uint8)

        self.img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    def scan_callback(self, msg):

        self.R = np.array(msg.ranges)
        self.intens = np.array(msg.intensities)

        x = self.R*np.cos(np.linspace(0, 2*np.pi, 360))
        y = self.R*np.sin(np.linspace(0, 2*np.pi, 360))
        z = np.zeros_like(x)

        self.xyz = np.concatenate([
            x.reshape([-1, 1]),
            y.reshape([-1, 1]),
            z.reshape([-1, 1])
        ], axis=1)

    def timer_callback(self):

        if self.xyz is not None and self.img is not None :
            
            xyz_p = self.xyz[np.where(self.xyz[:, 0]>=0)]


            intens_p = self.intens.reshape([-1,1])
            intens_p = intens_p[np.where(self.xyz[:, 0]>=0)]

            xyz_c = self.l2c_trans.transform_lidar2cam(xyz_p)

            xy_i = self.l2c_trans.project_pts2img(xyz_c, crop=True)

            img_l2c = draw_pts_img(self.img, xy_i[:, 0].astype(np.int32),
                                            xy_i[:, 1].astype(np.int32))
                                                
            cv2.imshow("Lidar2Cam", img_l2c)
            cv2.waitKey(1)

        else:
            pass


def main(args=None):

    rclpy.init(args=args)

    calibrator = SensorCalib()

    rclpy.spin(calibrator)


if __name__ == '__main__':

    main()