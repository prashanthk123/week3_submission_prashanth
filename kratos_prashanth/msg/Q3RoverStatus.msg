#This represents all relevant statuses of the rover at some time


#includes the linear and angular velocity of the rover
geometry_msgs/Twist twist

#Distance travelled in the time since start
float64 distance_travelled

#Current world coordinates of the rover
geometry_msgs/Pose pose

#Current battery power lever of the rover
float64 battery

#Time elapsed since boot
float64 time