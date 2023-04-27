#include <memory>
#include <iostream>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "tutorial_interfaces/msg/num.hpp"     // CHANGE

using std::placeholders::_1;
using namespace std;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber")
  {
    sub_ = this->create_subscription<std_msgs::msg::String>(
      "msg", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));

    custom_sub = this->create_subscription<tutorial_interfaces::msg::Num>(         
      "my_msg", 10, std::bind(&MinimalSubscriber::custom_callback, this, _1));
  }

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
  {
    RCLCPP_INFO(this->get_logger(), "I heard: %s", msg->data.c_str());    
    cout << msg->data << '\n';
  }


  void custom_callback(const tutorial_interfaces::msg::Num::SharedPtr msg) const      
  {
    RCLCPP_INFO(this->get_logger(), "Custom: %d", msg->num);              
    cout << msg->num << "\n";
    
  }
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_;
  rclcpp::Subscription<tutorial_interfaces::msg::Num>::SharedPtr custom_sub;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}