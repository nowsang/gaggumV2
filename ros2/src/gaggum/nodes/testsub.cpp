#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include "gaggum_msgs/msg/test.hpp"
#include "gaggum_msgs/msg/detection.hpp"

using std::placeholders::_1;
using namespace std;

class MinimalSubscriber : public rclcpp::Node
{
  public:
    MinimalSubscriber()
    : Node("minimal_subscriber")
    {
      subscription_ = this->create_subscription<gaggum_msgs::msg::Test>(
      "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));

      sub_ = this->create_subscription<gaggum_msgs::msg::Detection>(
      "yolo", 10, std::bind(&MinimalSubscriber::yolo_callback, this, _1));

      motor_sub = this->create_subscription<std_msgs::msg::Int32>(
      "motor_sub", 10, std::bind(&MinimalSubscriber::motor_callback, this, _1));

      motor_end = this->create_subscription<std_msgs::msg::Int32>(
      "end_pub", 10, std::bind(&MinimalSubscriber::end_callback, this, _1));

    }

  private:
    void topic_callback(const gaggum_msgs::msg::Test::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard: '%d'", msg->num);
    }

    void yolo_callback(const gaggum_msgs::msg::Detection::SharedPtr msg) const
    {
      int int_yolo_msg = msg->num_index;
      cout << int_yolo_msg << '\n';

    }

    void motor_callback(const std_msgs::msg::Int32::SharedPtr msg) const
    {
      cout << "motor" << '\n';
      int motor_msg = msg->data;
      cout << motor_msg << '\n';
    }

    void end_callback(const std_msgs::msg::Int32::SharedPtr msg) const
    {
      cout << "end" << '\n';
      int end_msg = msg->data;
      cout << end_msg << '\n';

    }


    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr motor_sub;
    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr motor_end;
    rclcpp::Subscription<gaggum_msgs::msg::Detection>::SharedPtr sub_;
    rclcpp::Subscription<gaggum_msgs::msg::Test>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}