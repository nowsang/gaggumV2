#include <iostream>
#include <memory>
#include <string>
#include <map>

#include "rclcpp/rclcpp.hpp"
#include <sio_client.h>

using namespace std;

class Time15 : public rclcpp::Node
{
public:
  Time15() : Node("time_15"), once(false)
  {    
    sio_client_.set_open_listener(std::bind(&Time15::on_connected, this));
    // sio_client_.connect("http://localhost:3001");
    sio_client_.connect("https://k8b101.p.ssafy.io:3001");

    
    timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&Time15::send_message, this));
  }

private:
  bool once;

  void on_connected()
  {
    RCLCPP_INFO(this->get_logger(), "Connected to Socket.IO server!");
  }

  void send_message()
  {    
    sio::message::list msg;

    if (!once) {
      once = true;
      map<string, int> hour = {{"hour", 15}};
      auto obj_msg = sio::object_message::create();
      for (const auto& [key, value] : hour) {
          // value is Int type. -> sio::int_message
          obj_msg->get_map()[key] = sio::int_message::create(value);
      }    
      msg.push(obj_msg);
      sio_client_.socket()->emit("time_control", msg);

      // Log the sent message
      RCLCPP_INFO(this->get_logger(), "Sent message to Socket.IO server: 'Hello from ROS 2!'");
    }
    
  }

  sio::client sio_client_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<Time15>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
