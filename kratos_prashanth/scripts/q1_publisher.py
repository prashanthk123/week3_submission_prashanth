#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldPublisher(Node):

    def __init__(self):
        super().__init__("q1_pub")
        self.publisher=self.create_publisher(String,"/new",10)
        self.timer=self.create_timer((1.0/15.0),self.timer_callback)

    def timer_callback(self):
        #called every (1/15) ~= 0.066s 
        #publishes "hello world" to /new
        msg=String()
        msg.data="Hello World !"
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node=HelloWorldPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()