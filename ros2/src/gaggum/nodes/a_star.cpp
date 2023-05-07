#include <iostream>
#include <queue>

#include "rclcpp/rclcpp.hpp"
#include "nav_msgs/msg/odometry.hpp"

using namespace std;
using std::placeholders::_1;

class AStar : public rclcpp::Node
{
  public:
    AStar()
    : Node("a_star")
    {
      // a_star_pub = this->create_publisher<gaggum_msgs::msg::Test>("topic", 10);
      // a_star_timer_ = this->create_wall_timer(500ms, std::bind(&AStar::timer_callback, this));

      odom_sub = this->create_subscription<nav_msgs::msg::Odometry>(
        "/odom", 10, bind(&AStar::odom_callback, this, _1));
      odom_sub = this->create_subscription<nav_msgs::msg::Odometry>(
        "/odom", 10, bind(&AStar::odom_callback, this, _1));
    }

  private:
    void odom_callback(const nav_msgs::msg::Odometry::SharedPtr msg) const
    {
      double odom_msg = msg->pose.pose.position.x;
      cout << odom_msg << endl; 
    }
    rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr odom_sub;
};

// void aStar(start)
// {
//  // 최소 힙을 구현할 변수들
//   auto cmp = [](int left, int right){ return left > right; };
//   priority_queue<int, vector<int>, decltype(cmp)> min_heap(cmp); 

//   min_heap.push(start);
//   cout << "point" << endl;
//   while (!min_heap.empty()) {
//     cout << min_heap.top() << " ";
//     min_heap.pop();
//   }
//   cout << endl;
// }

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<AStar>());
  rclcpp::shutdown();
  return 0;
}