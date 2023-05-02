
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using namespace std::chrono_literals;
using namespace std;

class TurtlebotController : public rclcpp::Node
{
public:
  TurtlebotController()
  : Node("turtlebot_controller")
  {
    move_pub = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
    move_timer = this->create_wall_timer(2000ms, std::bind(&TurtlebotController::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto twist_msg = geometry_msgs::msg::Twist();
    twist_msg.linear.x = 0.2;
    // twist_msg.angular.z = 0.2;

    move_pub->publish(twist_msg);
    cout << twist_msg.linear.x << "\n";
    
  }

  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr move_pub;
  rclcpp::TimerBase::SharedPtr move_timer;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto controller = std::make_shared<TurtlebotController>();
  rclcpp::spin(controller);
  rclcpp::shutdown();

  return 0;
}
