#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move():
    
    #initialize a node
    rospy.init_node('move_twist', anonymous=False) 
    
    #creates a publisher
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
    
    #creates a Twist message with linear and angular values.
    msg = Twist()
    msg.linear.x = 1.0
    msg.angular.z = 1.0
    
    #save current time and publish rate at 10 Hz.
    start = rospy.Time.now()
    rate = rospy.Rate(10)
    
    #publish for 5 seconds.
    while rospy.Time.now() < start + rospy.Duration.from_sec(5):
        pub.publish(msg)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass