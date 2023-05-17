import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient

def send_goal_pose(x, y, theta):
    rclpy.init()
    node = rclpy.create_node('goal_publisher')

    # Navigation2의 목표 위치로 이동하기 위한 액션 클라이언트 생성
    action_client = ActionClient(node, NavigateToPose, 'navigate_to_pose')

    # 목표 위치를 설정하기 위한 메시지 생성
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.orientation.z = theta

    # 액션 클라이언트로 목표 위치를 전송
    goal_msg = NavigateToPose.Goal()
    goal_msg.pose = goal_pose
    future = action_client.send_goal_async(goal_msg)

    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        result = future.result().result
        if result.result:
            print("목표 위치로 이동 성공!")
        else:
            print("목표 위치로 이동 실패.")
    else:
        print("목표 위치로 이동 실패.")

    node.destroy_node()
    rclpy.shutdown()

# 목표 위치 설정 (예시)
goal_x = 0.5
goal_y = 0.0
goal_theta = -1.0

# 목표 위치로 이동
send_goal_pose(goal_x, goal_y, goal_theta)
