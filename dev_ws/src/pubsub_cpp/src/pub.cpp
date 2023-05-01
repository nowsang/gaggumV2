#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "tutorial_interfaces/msg/num.hpp"

using namespace std::chrono_literals;
// using namespace std;

class MyPublisher : public rclcpp::Node
{
    public:
    MyPublisher()
    : Node("my_publisher"), count_(0)
    {
        pub_ = this->create_publisher<std_msgs::msg::String>("msg", 10);
        custom_pub = this->create_publisher<tutorial_interfaces::msg::Num>("my_msg", 10);
        timer_ = this->create_wall_timer(
            1000ms, std::bind(&MyPublisher::timer_callback, this));
        custom_timer = this->create_wall_timer(
            1000ms, std::bind(&MyPublisher::custom_timer_callback, this));
    }

    private:
    void custom_timer_callback()
    {
        int res = 1;
        auto message = tutorial_interfaces::msg::Num();              
        // message.num = this->count_++;                             
        message.num = res;                                       
        RCLCPP_INFO(this->get_logger(), "My Custom Publishing: %d", message.num);  
        custom_pub->publish(message);
    }

    void timer_callback()
    {
        auto msg = std_msgs::msg::String();
        msg.data = "Hello, world! " + std::to_string(count_++);
        RCLCPP_INFO(this->get_logger(), "Publishing: %s", msg.data.c_str());
        pub_->publish(msg);

    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::TimerBase::SharedPtr custom_timer;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_;
    rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr custom_pub;       
    size_t count_;
    
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MyPublisher>());
  rclcpp::shutdown();
  return 0;
}