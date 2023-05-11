// #include <iostream>
// #include <queue>
// #include <vector>

// #include "rclcpp/rclcpp.hpp"
// #include "nav_msgs/msg/occupancy_grid.hpp"
// #include "nav_msgs/msg/odometry.hpp"

// using namespace std;
// using std::placeholders::_1;

// class AStar : public rclcpp::Node
// {
//   public:
//     AStar() : Node("a_star")
//     {
//       // a_star_pub = this->create_publisher<gaggum_msgs::msg::Test>("topic", 10);
//       // a_star_timer_ = this->create_wall_timer(500ms, std::bind(&AStar::timer_callback, this));

//       grid_sub = this->create_subscription<nav_msgs::msg::OccupancyGrid>(
//         "/map", 10, bind(&AStar::grid_callback, this, _1));
        
//       odom_sub = this->create_subscription<nav_msgs::msg::Odometry>(
//         "/odom", 10, bind(&AStar::odom_callback, this, _1));
//     }

//   private:
//     void grid_callback(const nav_msgs::msg::OccupancyGrid::SharedPtr msg) const
//     {
//       // int8_t grid_msg = msg->vecter<int8_t>date;
//       cout << msg << endl;
//       cout << "123" << endl;
//     }
//     void odom_callback(const nav_msgs::msg::Odometry::SharedPtr msg) const
//     {
//       double odom_msg = msg->pose.pose.position.x;
//       // cout << odom_msg << endl; 
//     }
//     rclcpp::Subscription<nav_msgs::msg::OccupancyGrid>::SharedPtr grid_sub;
//     rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr odom_sub;


//   // 사용할 변수들
//   bool is_grid_update = false;

//   // 맵 데이터 행렬로 바꾸기
//   // void grid_update() {
//   //     is_grid_update = true;
      
//   //     int map_size = map_msg.data.size();
//   //     int grid_size = 350;
      
//   //     int num_rows = grid_size;
//   //     int num_cols = grid_size;
      
//   //     int index = 0;
      
//   //     int* map_to_grid = new int[map_size];
//   //     for(int i=0; i<map_size; i++) {
//   //         map_to_grid[i] = map_msg.data[i];
//   //     }
      
//   //     int* grid = new int[num_rows * num_cols];
//   //     for(int i=0; i<num_rows; i++) {
//   //         for(int j=0; j<num_cols; j++) {
//   //             grid[i * num_cols + j] = map_to_grid[index++];
//   //         }
//   //     }
      
//   //     delete[] map_to_grid;
//   // }

//   // void aStar(start)
//   // {
//   //  // 최소 힙을 구현할 변수들
//   //   auto cmp = [](int left, int right){ return left > right; };
//   //   priority_queue<int, vector<int>, decltype(cmp)> min_heap(cmp); 
//   //   min_heap.push(start);
//   //   cout << "point" << endl;
//   //   while (!min_heap.empty()) {
//   //     cout << min_heap.top() << " ";
//   //     min_heap.pop();
//   //   }
//   //   cout << endl;
//   // }
// };

// int main(int argc, char * argv[])
// {
//   rclcpp::init(argc, argv);
//   rclcpp::spin(std::make_shared<AStar>());
//   rclcpp::shutdown();
//   return 0;
// }