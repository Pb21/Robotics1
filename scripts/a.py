#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import sys
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


if __name__ == '__main__':

       rospy.init_node('tf_turtle')

       #Once the listener is created, it starts receiving tf transformations over the wire, and buffers them for up to 10 seconds.
       listener1 = tf.TransformListener()      
       turtle_vel = rospy.Publisher('robot_1/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)           
       rate = rospy.Rate(10.0)
       rospy.sleep(rospy.Duration(2.0))

       while not rospy.is_shutdown():
           cmd = geometry_msgs.msg.Twist()                
	   try:
                now = rospy.Time.now()
            #    past = now - rospy.Duration(1.0)
		
           #     listener1.waitForTransformFull("/robot_1", now,
            #                              "/robot_0", past,
             #                             "/world", rospy.Duration(3.0))
              #  (trans,rot) = listener1.lookupTransformFull("/robot_1", now,
               #                           "/robot_0", past,
                #                          "/world")
	#	listener1.waitForTransformFull("/robot_1", now,
         #                                 "/robot_0", past,
          #                                "/world", rospy.Duration(3.0))
		listener.waitForTransform("/robot_1", "/robot_0", now, rospy.Duration(1.0))
                (trans,rot) = listener1.lookupTransform("/robot_1","/robot_0",rospy.Time(0))
		
           	angular = 4 * math.atan2(trans[1], trans[0])
           	linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)

           	cmd.linear.x = linear
           	cmd.angular.z = angular
	
           	turtle_vel.publish(cmd)
           except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException,tf.Exception):
		rospy.loginfo(sys.exc_info())
		print "exx"
                continue
   	   
           angular = 4 * math.atan2(trans[1], trans[0])
           linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
           #cmd = geometry_msgs.msg.Twist()
           cmd.linear.x = linear
           cmd.angular.z = angular

           turtle_vel.publish(cmd)   
           rate.sleep()
