#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup

#S1 node
class Signal1(Node):

    def __init__(self):
        super().__init__("S1")
        self.signal=String()
        self.signal.data="red"
        self.s1_publisher=self.create_publisher(String,"/s1",10)
        self.timer=self.create_timer(10,self.timer_callback)

    def timer_callback(self):
        #publishes green/red alternating once every 10 seconds to s1
        if self.signal.data=="green":self.signal.data="red"
        else:self.signal.data="green"
        self.get_logger().info(self.signal.data+" published to s1")
        self.s1_publisher.publish(self.signal)


#S2 node
class Signal2(Node):

    def __init__(self):
        super().__init__("S2")
        self.s1_subscription=self.create_subscription(String,"/s1",self.s1_callback,10)
        self.s2_publisher=self.create_publisher(String,"/s2",10)

    def s1_callback(self,s1_msg:String):
        #called when subscriber receives from /s1 
        #sends green when /s1 reads red and vice versa to /s2
        s2_msg=String()
        if s1_msg.data=="red":s2_msg.data="green"
        else:s2_msg.data="red"
        self.s2_publisher.publish(s2_msg)
        self.get_logger().info(str(s2_msg.data)+" published to s2")


def main(args=None):
    rclpy.init(args=args)

    node1=Signal1()
    node2=Signal2()
    #parallel run
    executor=MultiThreadedExecutor()
    executor.add_node(node1)
    executor.add_node(node2)
    executor.spin()

    node1.destroy_node()
    node2.destroy_node()   
    rclpy.shutdown()

if __name__=="__main__":
    main()