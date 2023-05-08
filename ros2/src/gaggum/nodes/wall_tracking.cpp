#include <iostream>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "nav_msgs/msg/odometry.hpp"

using std::placeholders::_1;
// using std::placeholders::_2;
using namespace std::chrono_literals;
using namespace std;

class WallTracking : public rclcpp::Node
{
    public:
        WallTracking() : Node("wall_tracking_node"), my_int(1), is_odom(false), is_path(false), is_status(false)
        {
            cmd_pub = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
            cmd_sub = this->create_subscription<geometry_msgs::msg::Twist>(
                "/cmd_vel", 10, std::bind(&WallTracking::cmd_callback, this, _1)
            );
            lidar_sub = this->create_subscription<sensor_msgs::msg::LaserScan>(
                "/scan", 10, std::bind(&WallTracking::lidar_callback, this, _1)
            );
            odom_sub = this->create_subscription<nav_msgs::msg::Odometry>(
                "/odom", 10, std::bind(&WallTracking::odom_callback, this, _1)
            );

            timer_ = this->create_wall_timer(1000ms, std::bind(&WallTracking::timer_callback, this));

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

        void timer_callback()
        {            
            cout << is_odom << '\n';
            // my_int = 0;
        }

        void odom_callback(const nav_msgs::msg::Odometry::SharedPtr msg) const
        {
            float odom_msg = msg->pose.pose.orientation.w;
            cout << odom_msg << '\n';
        }

        int my_int;
        bool is_odom;
        bool is_path;
        bool is_status;

        rclcpp::TimerBase::SharedPtr timer_;        
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_pub;        
        rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr odom_sub;
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