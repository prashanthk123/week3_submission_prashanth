#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldSubscriber(Node):

    def __init__(self):
        super().__init__("q1_sub")
        self.publisher=self.create_subscription(String,"/new",self.pub_callback,10)

    def pub_callback(self,msg:String):
        #reads from /new and prints to terminal
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node=HelloWorldSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()