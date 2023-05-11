// #include "rclcpp/rclcpp.hpp"
// #include "geometry_msgs/msg/pose_stamped.hpp"
// #include "nav2_msgs/action/navigate_to_pose.hpp"

// using namespace std;
// using namespace std::chrono_literals;

// class GoalSender : public rclcpp::Node
// {
//     public:
//         GoalSender() : Node("goal_sender")
//         {
//             publisher_ = this->create_publisher<geometry_msgs::msg::PoseStamped>("/goal_pose", 10);
//             timer = this->create_wall_timer(
//                 500ms, std::bind(&MinimalPublisher::timer_callback, this)
//             )
//         }

//     private:
//         void timer_callback()
//         {
//             auto goal_msg = geometry_msgs::msg::PoseStamped();
//             goal_msg_.header.frame_id = "map"; // 목표 위치가 지정된 map frame
//             goal_msg_.pose.position.x = 0.65; // 목표 지점의 x 좌표
//             goal_msg_.pose.position.y = -1.77; // 목표 지점의 y 좌표
//             goal_msg_.pose.orientation.w = 1.0; // 목표 방향 지정
//             cout << goal_msg << endl;

//         }
//         rclcpp::Publisher<geometry_msgs::msg::PoseStamped>::SharedPtr goal_msg;
//         rclcpp::TimerBase::SharedPtr timer;
// };

// int main(int argc, char * argv[])
// {
//     rclcpp::init(argc, argv);
//     auto node = std::make_shared<GoalSender>();
//     node->send_goal();
//     rclcpp::spin(node);
//     rclcpp::shutdown();
//     return 0;
// }