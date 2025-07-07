#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from std_msgs.msg import *


class Timer(Node):

    def __init__(self):
        super().__init__("timer")
        self.seconds=0
        self.minutes=0
        self.hours=0
        #publisher defn
        self.seconds_pub=self.create_publisher(Int32,"/second",10)
        self.minutes_pub=self.create_publisher(Int32,"/minute",10)
        self.hours_pub=self.create_publisher(Int32,"/hour",10)
        self.time_pub=self.create_publisher(String,"/clock",10)

        self.timer=self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        
        time=String()
        temp=Int32()

        #updates
        self.seconds+=1
        self.minutes+=(self.seconds//60)
        self.hours+=(self.minutes//60)
        self.seconds=self.seconds%60
        self.minutes=self.minutes%60
        self.hours=self.hours%24
        
        #publishing to various topics 
        temp.data=int(self.seconds)
        self.seconds_pub.publish(temp)          # /second
        temp.data=int(self.minutes)
        self.minutes_pub.publish(temp)          # /minute
        temp.data=int(self.hours)
        self.hours_pub.publish(temp)            # /hour
        time.data=str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds)
        self.time_pub.publish(time)             # /clock
            

def main(args=None):
    
    rclpy.init(args=args)
    node=Timer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()