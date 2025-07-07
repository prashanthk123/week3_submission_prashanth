# week3_submission_prashanth

All python scripts are under the scripts directory, action file in the action directory and custom msgs in msg directory

Question 1:
----------

The Publisher node is written in q1_publisher.py and the Subscriber node in q1_subscriber.py

Question 2:
------------

The Signals S1 and S2 are 2 seperate nodes both present in the q2.py file running in parallel using a multithreaded executor

Question 3:
------------
The custom message is defined as Q3RoverStatus and is in the msg dir


Question 4:
------------
The timer Node in q4.py controls the logic for the clock, updates seconds every second and publishes each component to respective topics

RQT GRAPH:
------------
![Screenshot from 2025-07-07 23-06-00](https://github.com/user-attachments/assets/13fadd9d-a342-4dde-a4a5-46b40e2887c3)


Bonus Question:
------------
Action server defined in BonusQ_ActionServer.py
Action Client defined in BonusQ_ActionClient.py
Action defined as RobotArmKinematics.action present in the action directory

