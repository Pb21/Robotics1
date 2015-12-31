#!/usr/bin/env python
import numpy
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def listener():
    rospy.Subscriber("/base_scan", LaserScan, talker)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def talker(data):
    pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
    rate = rospy.Rate(10) # 10hz
    r = data.ranges
    msg = Twist()
    flag=1
    for i in range(361):
    	if r[i] < 1.0:
	   print "crash"
	   msg.angular.z=8.8
           msg.linear.x=0.0
	   flag=0 
	   break 
    if flag!=0:
    	msg.linear.x = 2.0
    	msg.angular.z = 0.0

    pub.publish(msg)	        
    rate.sleep()

if __name__ == '__main__':
    rospy.init_node('evader', anonymous=True)
    while not rospy.is_shutdown():
	listener()
