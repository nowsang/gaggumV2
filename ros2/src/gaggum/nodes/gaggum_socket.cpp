#include <iostream>
#include <memory>
#include <string>
#include <map>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include "gaggum_msgs/msg/map_scan.hpp"
#include <sio_client.h>

using namespace std;
using std::placeholders::_1;


class GaggumSocketNode : public rclcpp::Node
{
public:
  GaggumSocketNode() : Node("socketiosub_node")
  {

    move_state = this->create_publisher<std_msgs::msg::Int32>("motor", 10);
    map_scan_pub = this->create_publisher<gaggum_msgs::msg::MapScan>("MapScan", 10);
    map_scan_sub = this->create_subscription<gaggum_msgs::msg::MapScan>(
      "MapScan", 10, std::bind(&GaggumSocketNode::map_scan_callback, this, _1));
    motor_end_sub = this->create_subscription<std_msgs::msg::Int32>(
      "motor_end", 10, std::bind(&GaggumSocketNode::motor_end_callback, this, _1));
    
    // Connect to the Socket.IO server
    sio_client_.set_open_listener(std::bind(&GaggumSocketNode::on_connected, this));
    // sio_client_.connect("http://localhost:3001");
    sio_client_.connect("https://k8b101.p.ssafy.io:3001");
    

    // motor control
    sio_client_.socket()->on("run_motor", [this](sio::event& event) {  
      
      cout << "motor control" << "\n";

      auto motor_control = event.get_message()->get_map();
      string mode = motor_control["mode"]->get_string();      
      
      
      // motor 1, 2, 3
      if (mode == "motor_status") {        
        int motor = motor_control["motor"]->get_int();
        cout << motor << '\n';

        auto motor_msg = std_msgs::msg::Int32();
        motor_msg.data = motor;
        move_state->publish(motor_msg);
      }

      // else if (mode == "water_end")



    //   cout << event.get_message()->get_int() << "\n";

    //   int motor_data = event.get_message()->get_int();

    //   auto motor_msg = std_msgs::msg::Int32();
    //   motor_msg.data = motor_data;
    //   move_state->publish(motor_msg);

    //   sio::message::list socket_msg;
    //   // plant1, plant2, plant3

    // //   move_state->publish(event.get_message()->get_int());
    //   // mode = 1 ;
    //   if (motor_data == -1) {        
    //     map<string, string> plant = {{"mode", "water_end"}, {"plant", "plant1"}};
    //     auto obj_msg = sio::object_message::create();
    //     for (const auto& [key, value] : plant) {
    //     // value is Int type. -> sio::int_message
    //     obj_msg->get_map()[key] = sio::string_message::create(value);
    //     }
    //     socket_msg.push(obj_msg);        

    //     sio_client_.socket()->emit("run_motor", socket_msg);
    //   }


    });

    //map scan
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

  void map_scan_callback(const gaggum_msgs::msg::MapScan::SharedPtr msg)
  {
    sio::message::list socket_msg;
    cout << "Map Scan Data" << '\n';
    // int scan_msg = msg->run;
    auto scan_msg = sio::int_message::create(msg->run);
    socket_msg.push(scan_msg);
    if (msg->run == -1) {
      cout << "Here!!!!!!!!!!!!!!" << "\n";
      sio_client_.socket()->emit("run_walltracking", socket_msg);
    }
  }

  void motor_end_callback(const std_msgs::msg::Int32::SharedPtr msg)
  {
    sio::message::list socket_msg;
    cout << "motor_end" << '\n';

    map<string, string> watering_plant = {{"mode", "water_end"}, {"plant", "plant1"}};
    auto end_msg = sio::object_message::create();
    for (const auto& [key, value] : plant) {
        // value is Int type. -> sio::int_message
        obj_msg->get_map()[key] = sio::string_message::create(value);
    }   
    socket_msg.push(end_msg);
    sio_client_.socket()->emit("run_motor", socket_msg)

  }


  sio::client sio_client_;
  rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr move_state;
  rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr motor_end_sub;
  rclcpp::Publisher<gaggum_msgs::msg::MapScan>::SharedPtr map_scan_pub; 
  rclcpp::Subscription<gaggum_msgs::msg::MapScan>::SharedPtr map_scan_sub;

};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<GaggumSocketNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}