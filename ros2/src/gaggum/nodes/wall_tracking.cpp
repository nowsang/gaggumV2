#include <iostream>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include "geometry_msgs/msg/twist.hpp"

using std::placeholders::_1;
using std::placeholders::_2;
using namespace std::chrono_literals;
using namespace std;

class WallTracking : public rclcpp::Node
{
    public:
        WallTracking() : Node("wall_tracking_node")
        {
            cmd_pub = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
            cmd_sub = this->create_subscription<geometry_msgs::msg::Twist>(
            "/cmd_vel", 10, std::bind(&WallTracking::cmd_callback, this, _1)
            );
            lidar_sub = this->create_subscription<sensor_msgs::msg::LaserScan>(
            "/scan", 10, std::bind(&WallTracking::lidar_callback, this, _1)
            );

        }
    private:
        void lidar_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg) const
        {
            float lidar_msg = msg->angle_min;
            cout << lidar_msg << "\n";
        }
        void cmd_callback(const geometry_msgs::msg::Twist::SharedPtr msg) const
        {
            float velocity = msg->linear.x;
            cout << "cmd_callback" << " " << velocity << '\n';
        }

        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_pub;        
        rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr cmd_sub;
        rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr lidar_sub;        

};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<WallTracking>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}