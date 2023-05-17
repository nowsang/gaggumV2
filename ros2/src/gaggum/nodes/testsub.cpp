#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include "gaggum_msgs/msg/map_scan.hpp"
#include "gaggum_msgs/msg/detection.hpp"
#include "gaggum_msgs/msg/plant_info.hpp"

using std::placeholders::_1;
using namespace std;

class MinimalSubscriber : public rclcpp::Node
{
  public:
    MinimalSubscriber()
    : Node("minimal_subscriber")
    {
      subscription_ = this->create_subscription<gaggum_msgs::msg::MapScan>(
      "MapScan", 10, std::bind(&MinimalSubscriber::scan_callback, this, _1));

      sub_ = this->create_subscription<gaggum_msgs::msg::Detection>(
      "yolo", 10, std::bind(&MinimalSubscriber::yolo_callback, this, _1));

      plant_info_sub = this->create_subscription<gaggum_msgs::msg::PlantInfo>(
      "waterPlant", 10, std::bind(&MinimalSubscriber::plantinfo_callback, this, _1));

      motor_end = this->create_subscription<std_msgs::msg::Int32>(
      "end_motor", 10, std::bind(&MinimalSubscriber::end_callback, this, _1));

    }

  private:
    void scan_callback(const gaggum_msgs::msg::MapScan::SharedPtr msg) const
    {
      int scan_msg = msg->run;
      cout << scan_msg << "\n";
      // RCLCPP_INFO(this->get_logger(), "I heard: '%d'", msg->num);
    }

    void yolo_callback(const gaggum_msgs::msg::Detection::SharedPtr msg) const
    {
      int int_yolo_msg = msg->num_index;
      cout << int_yolo_msg << '\n';

    }

    void plantinfo_callback(const gaggum_msgs::msg::PlantInfo::SharedPtr msg) const
    {
      cout << "plantInfo" << '\n';
      int plant_id = msg->plant_id;
      cout << plant_id << '\n';
    }

    void end_callback(const std_msgs::msg::Int32::SharedPtr msg) const
    {
      cout << "end" << '\n';
      int end_msg = msg->data;
      cout << end_msg << '\n';

    }


    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr motor_end;
    rclcpp::Subscription<gaggum_msgs::msg::Detection>::SharedPtr sub_;
    rclcpp::Subscription<gaggum_msgs::msg::MapScan>::SharedPtr subscription_;
    rclcpp::Subscription<gaggum_msgs::msg::PlantInfo>::SharedPtr plant_info_sub;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}