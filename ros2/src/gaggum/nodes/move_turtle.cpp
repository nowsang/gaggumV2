
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include "geometry_msgs/msg/twist.hpp"

using std::placeholders::_1;
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
    move_state = this->create_publisher<std_msgs::msg::Int32>("motor_sub", 10);
    openCR_sub = this->create_subscription<std_msgs::msg::Int32>(
      "sonar_pub", 10, std::bind(&TurtlebotController::sonar_callback, this, _1));


    // auto state_msg = std_msgs::msg::Int32();
    // state_msg.data = 4;
    // move_state->publish(state_msg);
    // cout << "number 4 play" << '\n';

  }

private:
  void timer_callback()
  {
    
    auto state_msg = std_msgs::msg::Int32();
    state_msg.data = 3;
    move_state->publish(state_msg);
    cout << state_msg.data << '\n';


    // auto twist_msg = geometry_msgs::msg::Twist();
    // twist_msg.linear.x = 0.1;
    // // twist_msg.angular.z = 0.2;

    // move_pub->publish(twist_msg);
    // cout << twist_msg.linear.x << "\n";    
  }
  
  void sonar_callback(const std_msgs::msg::Int32::SharedPtr msg) const
  {
    int sonar_msg = msg->data;
    cout << sonar_msg << '\n';
  }


  rclcpp::TimerBase::SharedPtr move_timer;
  rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr move_state;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr move_pub;
  rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr openCR_sub;

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto controller = std::make_shared<TurtlebotController>();
  rclcpp::spin(controller);
  rclcpp::shutdown();

  return 0;
}
