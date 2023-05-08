#include <iostream>
#include <memory>
#include <string>
#include <map>

#include "rclcpp/rclcpp.hpp"
// #include "../../socket.io-client-cpp/src/sio_client.h"
#include <sio_client.h>

using namespace std;

class SocketIONode : public rclcpp::Node
{
public:
  SocketIONode() : Node("socketio_node")
  {
    // Connect to the Socket.IO server
    sio_client_.set_open_listener(std::bind(&SocketIONode::on_connected, this));
    // sio_client_.connect("http://localhost:3001");
    sio_client_.connect("https://k8b101.p.ssafy.io/socket");

    // Create a timer to send messages to the server periodically
    timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&SocketIONode::send_message, this));
  }

private:
  void on_connected()
  {
    RCLCPP_INFO(this->get_logger(), "Connected to Socket.IO server!");
  }

  void send_message()
  {
    // Send a message to the server 
    // 소켓 통신을 위한 msg 생성(default)
    sio::message::list msg;

    // string
    // msg.push("Hello from ROS 2!");    
    
    // int
    // auto int_msg = sio::int_message::create(33);
    // msg.push(int_msg);

    // bool
    // auto bool_msg = sio::bool_message::create(false);
    // msg.push(bool_msg);

    // map
    map<string, int> plant = {{"plant1", 1}, {"plant2", 2}, {"plant3", 3}};
    auto obj_msg = sio::object_message::create();
    for (const auto& [key, value] : plant) {
        // value is Int type. -> sio::int_message
        obj_msg->get_map()[key] = sio::int_message::create(value);
    }    
    msg.push(obj_msg);


    sio_client_.socket()->emit("message", msg);

    // Log the sent message
    RCLCPP_INFO(this->get_logger(), "Sent message to Socket.IO server: 'Hello from ROS 2!'");
  }

  sio::client sio_client_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SocketIONode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
