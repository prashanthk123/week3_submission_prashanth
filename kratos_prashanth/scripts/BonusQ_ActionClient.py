#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle
from kratos_prashanth.action import RobotArmKinematics


class ArmControlClientNode(Node):

    def __init__(self):
        super().__init__("action_client")
        self.goal=30
        self.action_client=ActionClient(
            self,
            RobotArmKinematics,
            "robot_arm",
        )

        self.send_goal()

    def send_goal(self):
        self.action_client.wait_for_server()
        goal=RobotArmKinematics.Goal()
        goal.goal_angle=self.goal
        self.action_client.send_goal_async(goal,feedback_callback=self.feedback_callback).add_done_callback(self.goal_response_callback)

    def goal_response_callback(self,future):
        self.goal_handle_:ClientGoalHandle=future.result()
        if self.goal_handle_.accepted:
            self.goal_handle_.get_result_async().add_done_callback(self.goal_result_callback)

    def goal_result_callback(self,future):
        result=future.result().result
        if(result):self.get_logger().info("success")
        else: self.get_logger().info("fail")

    def feedback_callback(self,feedback):
        feedback_msg:RobotArmKinematics.Feedback=feedback.feedback
        self.get_logger().info("Current angle is:"+str(feedback_msg.current_angle))


def main():
    rclpy.init(args=None)
    node=ArmControlClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()