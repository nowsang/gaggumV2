import rclpy
from nav2_msgs.action import NavigateToPose
from nav2_msgs.srv import ClearCostmaps, ClearCostmapsRequest

def send_goal(x, y, theta):
    rclpy.init()
    node = rclpy.create_node('send_goal')

    # Clear the costmaps to make sure there are no obstacles in the way
    clear_costmaps_client = node.create_client(ClearCostmaps, 'global_costmap/clear_costmaps')
    while not clear_costmaps_client.wait_for_service(timeout_sec=1.0):
        print('Service not available')
    clear_costmaps_request = ClearCostmapsRequest()
    clear_costmaps_future = clear_costmaps_client.call_async(clear_costmaps_request)

    # Create a NavigateToPose action client
    navigate_to_pose_client = node.create_client(NavigateToPose, 'navigate_to_pose')
    while not navigate_to_pose_client.wait_for_service(timeout_sec=1.0):
        print('Service not available')

    # Create a goal message
    goal_msg = NavigateToPose.Goal()
    goal_msg.pose.header.frame_id = 'map'
    goal_msg.pose.pose.position.x = x
    goal_msg.pose.pose.position.y = y
    goal_msg.pose.pose.orientation.z = theta

    # Send the goal
    navigate_to_pose_future = navigate_to_pose_client.send_goal_async(goal_msg)
    rclpy.spin_until_future_complete(node, navigate_to_pose_future)

    # Print the result
    if navigate_to_pose_future.result() is not None:
        print('Navigation succeeded')
    else:
        print('Navigation failed')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    send_goal(1.0, 2.0, 0.0)