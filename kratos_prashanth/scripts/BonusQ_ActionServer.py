#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionServer 
from rclpy.action.server import ServerGoalHandle
from kratos_prashanth.action import RobotArmKinematics
from rclpy.callback_groups import ReentrantCallbackGroup

class ArmControlServerNode(Node):

    def __init__(self):
        super().__init__("action_server")
        self.angle=0
        self.callback_grp=ReentrantCallbackGroup()
        self.action_server=ActionServer(
            self,
            RobotArmKinematics,
            "robot_arm",
            self.action_callback,
        )
        self.get_logger().info("node started")

    def action_callback(self,msg:ServerGoalHandle):
        feedback_msg=RobotArmKinematics.Feedback()
        while(self.angle!=msg.request.goal_angle!=self.angle):
            if self.angle<msg.request.goal_angle: 
                self.angle+=1
            else:
                self.angle-=1

            feedback_msg.current_angle=self.angle
            msg.publish_feedback(feedback_msg)
            time.sleep(1)

        result=RobotArmKinematics.Result()
        result.success=True
        msg.succeed()
        return result

def main(args=None):
    rclpy.init(args=args)
    node=ArmControlServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()