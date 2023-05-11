import rclpy
from rclpy.node import Node
from gaggum_msgs.msg import Tts
from gtts import gTTS
from playsound import playsound

import os

# bool water_mode
# bool sunny_mode
# string pot_name

class TTS(Node):
    
    def __init__(self):
        super().__init__('tts')

        self.tts_pub = self.create_publisher(Tts, '/tts', 10)        
        self.tts_sub = self.create_subscription(Tts, '/tts', self.tts_callback, 10)

        # publish도 필요함 끝났으면 끝났다는 정보를 어딘가에 전달해야하니까. Tts.msg에 end 변수도 넣을까.?
        # self.pub = self.create_publisher()
    
    
    def tts_callback(self,msg):
        # tts 사운드 상대경로 설정
        print('tts', msg)    
        os_file_path = os.path.abspath(__file__)        
        tts_path = os_file_path.replace('install\\gaggum\\Lib\\site-packages\\gaggum\\tts.py', 
                                        'ros2_smart_home\\gaggum\\sound')     
        
        # TTS 만들기(물주기/ 필요한 정보 : 모드)
        # pot_name = msg.pot_name
        # pot_name = "경섭"    # 변수 명으로 바꿔야함      
        # data = pot_name + ' 화분에 물 주는 중입니다.'
        if msg.shutter:
            tts_file = 'shutter.mp3'
            playsound(f'{tts_path}/{tts_file}')    
            msg.shutter = False

        if msg.water_mode or msg.sunny_mode:
            print('tts시작')
            if msg.water_mode:
                data = '화분에 물 주는 중입니다.'
                tts_file = 'water.mp3'
                playsound(f'{tts_path}/{tts_file}')
            elif msg.sunny_mode:
                data = '화분을 옮기는 중입니다.'
                tts_file = 'sunny.mp3'
                playsound(f'{tts_path}/{tts_file}')
            

            # sp = gTTS( lang='ko', text=data, slow=False )
            # sp.save(f'{tts_path}/{tts_file}')

            # playsound(f'{tts_path}/{tts_file}')

            # 다시 변수 초기화
            msg.water_mode = False
            msg.sunny_mode = False
            self.tts_pub.publish(msg)

        
        if msg.water_mode_end or msg.sunny_mode_end:
            print("이동 종료")

            if msg.water_mode_end:
                # data = '급수가 종료 되었습니다.'
                tts_file = 'waterEnd.mp3'
                playsound(f'{tts_path}/{tts_file}')
            elif msg.sunny_mode_end:
                data = '화분 옮기기가 종료 되었습니다.'
                tts_file = 'sunny_end.mp3'
            

            # ending = gTTS( lang='ko', text=data, slow=False )

            # ending.save(f'{tts_path}/{tts_file}')

            # playsound(f'{tts_path}/{tts_file}')

            msg.water_mode_end = False
            msg.sunny_mode_end = False
            self.tts_pub.publish(msg)







def main(args=None):
    rclpy.init(args=args)
    tts = TTS()
    rclpy.spin(tts)
    tts.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()