#include <iostream>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "gaggum_msgs/msg/map_scan.hpp"
#include <sio_client.h>

using namespace std;


class SocketIOSubNode : public rclcpp::Node
{
public:
  SocketIOSubNode() : Node("socketiosub_node")
  {
    // map_scan pub
    map_scan_pub = this->create_publisher<gaggum_msgs::msg::MapScan>("MapScan", 10);
    // map_scan_sub = this->create_subsc
    
    
    // Connect to the Socket.IO server
    sio_client_.set_open_listener(std::bind(&SocketIOSubNode::on_connected, this));
    sio_client_.connect("http://localhost:3001");
    // sio_client_.connect("https://k8b101.p.ssafy.io:3001");
    
    sio_client_.socket()->on("message", [](sio::event& event) {
    //   std::string data = event.get_message()->get_string();      
    //   RCLCPP_INFO(this->get_logger(), "Received message from Socket.IO server on /message: '%s'", data.c_str());
      cout << "assd" << "\n";

      // str
      // cout << event.get_message()->get_string() << "\n";

      // int
      cout << event.get_message()->get_int() << "\n";

      // bool
      // cout << event.get_message()->get_bool() << '\n';

      // map
      // auto custom_obj = event.get_message()->get_map();      
      // int plant1_value = custom_obj["plant1"]->get_int();
      // cout << plant1_value << '\n';


    });

    sio_client_.socket()->on("run_walltracking", [this](sio::event& event) {

      cout << "run_walltracking Socket" << "\n";
      
      // pusblish
      auto scan_msg = gaggum_msgs::msg::MapScan();
      scan_msg.run = event.get_message()->get_int();
      map_scan_pub->publish(scan_msg);



      cout << event.get_message()->get_int() << "\n";


    });

  }

private:
  void on_connected()
  {
    RCLCPP_INFO(this->get_logger(), "Connected to Socket.IO server!");
  }

  sio::client sio_client_;
  rclcpp::Publisher<gaggum_msgs::msg::MapScan>::SharedPtr map_scan_pub; 

};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SocketIOSubNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}