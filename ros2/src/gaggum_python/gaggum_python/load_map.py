import rclpy
import numpy as np
from rclpy.node import Node

import os
from geometry_msgs.msg import Pose
from squaternion import Quaternion
from nav_msgs.msg import Odometry,OccupancyGrid,MapMetaData
from math import pi

class loadMap(Node):

    def __init__(self):
        super().__init__('load_map')

        self.map_pub = self.create_publisher(OccupancyGrid, 'map', 1)
        
        time_period=1  
        self.timer = self.create_timer(time_period, self.timer_callback)
      
        self.map_msg = OccupancyGrid()
        self.map_size_x = 350
        self.map_size_y = 350
        self.map_resolution = 0.05
        self.map_offset_x = -8.75
        self.map_offset_y = -8.75
        self.map_data = [0 for i in range(self.map_size_x*self.map_size_y)]

        grid=np.array(self.map_data)
        grid=np.reshape(grid,(self.map_size_x , self.map_size_y))

        self.map_msg.header.frame_id="map"

        # 맵에 대한 정보를 넣는 과정같다.
        m = MapMetaData()
        m.resolution = self.map_resolution
        m.width = self.map_size_x
        m.height = self.map_size_y
        m.origin = Pose()
        m.origin.position.x = self.map_offset_x
        m.origin.position.y = self.map_offset_y

        self.map_meta_data = m
        self.map_msg.info=self.map_meta_data
        
        # 로직 2. 맵 데이터 읽고, 2차원 행렬로 변환
        full_path = os.path.abspath(__file__)
        # 상대경로로 작성
        full_path = full_path.replace('install/gaggum_python/lib/python3.8/site-packages/gaggum_python/load_map.py', 'src/gaggum_python/map/map.txt')
        # 읽기 모드로 열기
        self.f = open(full_path, 'r')
        line = self.f.readline()
        line_data = line.split()
        # str을 int로 변환 
        line_data = list(map(int, line_data))

        for num,data in enumerate(line_data):
            self.map_data[num] = data 

        map_to_grid = np.array(self.map_data)
        grid = np.reshape(map_to_grid, (self.map_size_x, self.map_size_y))
        # 로직 3. 점유영역 근처 필터처리
    
        for x in range(self.map_size_x):
            for y in range(self.map_size_y):
                # grid 영역이 100이면 장애물이 있다.
                if grid[x][y] == 100:
                    # 그 좌표를 127로 바꿔주고

                    for i in range(y-3, y+3):
                        if i < 0 or i >= self.map_size_y:
                            continue
                        if grid[x][i] != 100:
                            grid[x][i] = 127
                        for j in range(x-3, x+3):
                            if j < 0 or j >= self.map_size_x:
                                continue
                            if grid[j][i] != 100:
                                grid[j][i] = 127

        np_map_data=grid.reshape(1,self.map_size_x*self.map_size_y)

        # [[, , , , ,]] 형태로 만들어준다.
        list_map_data=np_map_data.tolist()

        self.f.close()
        # [[, , , , ,]] 형태에서 [] 벗겨내기
        self.map_msg.data=list_map_data[0]

        # 기존과 비교
        # self.map_msg.data=line_data

    def timer_callback(self):
        self.map_msg.header.stamp =rclpy.clock.Clock().now().to_msg()
        self.map_pub.publish(self.map_msg)

       
def main(args=None):
    rclpy.init(args=args)
    load_map = loadMap()
    rclpy.spin(load_map)
    load_map.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()