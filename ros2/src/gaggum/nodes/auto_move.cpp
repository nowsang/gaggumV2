#include <iostream>
#include <memory>
#include <string>
#include <map>

#include "rclcpp/rclcpp.hpp"
#include <sio_client.h>

using namespace std;


class AutoMoveNode : public rclcpp::Node
{
public:
  AutoMoveNode() : Node("auto_move_node")
  {
    // Connect to the Socket.IO server
    sio_client_.set_open_listener(std::bind(&AutoMoveNode::on_connected, this));
    sio_client_.connect("http://localhost:3001");
       
     z CCCCCCCCCCCCCCCC
    sio_client_.socket()->on("auto_move", [](sio::event& event) {
    //   std::string data = event.get_message()->get_string();      
      cout << "auto move" << "\n";

      // plant water INFO
      auto custom_obj = event.get_message()->get_map();      
      auto plant_info = custom_obj["data"]->get_vector();   
      for (int i = 0; i < plant_info.size(); i++) {        
        auto waterplant = plant_info[i]->get_map();
        //   int plant_id = plant_V["plant_id"]->get_int();
        //   string plant_name = plant_V["plant_name"]->get_string();    
        for (auto it : waterplant) {
            cout << it.first << " " << it.second << '\n';
        }
      } 

    });
  }

private:
  void on_connected()
  {
    RCLCPP_INFO(this->get_logger(), "Connected to Socket.IO server!");
  }

  sio::client sio_client_;

};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<AutoMoveNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}