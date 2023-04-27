// #include <iostream>
// #include <memory>
// #include <string>

// #include "rclcpp/rclcpp.hpp"
// #include "socket.io-client-cpp/src/sio_client.h"

// class SocketIONode : public rclcpp::Node
// {
// public:
//     SocketIONode() : Node("socketio_node")
//     {
//         // Connect to the Socket.IO server
//         sio_client_.set_open_listener(std::bind(&SocketIONode::on_connected, this));
//         sio_client_.connect("http://localhost:3001");

//         // Create a timer to send messages to the server periodically
//         timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&SocketIONode::send_message, this));
//     }

// private:
//     void on_connected()
//     {
//         RCLCPP_INFO(this->get_logger(), "Connected to Socket.IO server!");
//     }

//     void send_message()
//     {
//         // Send a message to the server
//         sio_client_.socket()->emit("message", "Hello from ROS 2!");

//         // Log the sent message
//         RCLCPP_INFO(this->get_logger(), "Sent message to Socket.IO server: 'Hello from ROS 2!'");
//     }

//     sio::client sio_client_;
//     rclcpp::TimerBase::SharedPtr timer_;
// };

// int main(int argc, char **argv)
// {
//     rclcpp::init(argc, argv);
//     auto node = std::make_shared<SocketIONode>();
//     rclcpp::spin(node);
//     rclcpp::shutdown();
//     return 0;
// }
