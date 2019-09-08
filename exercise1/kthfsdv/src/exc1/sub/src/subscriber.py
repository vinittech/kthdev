#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def result(msg):
    pub1 = rospy.Publisher('result', Int32, queue_size=10)
    rate1 = rospy.Rate(20)
    pub1.publish(msg)
    rate1.sleep()

def callback(data):
    msg = (data.data)/0.15
    rospy.loginfo(msg)
    result(msg)

def receive():
    rospy.init_node('receive', anonymous=True)
    rospy.Subscriber("jain", Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    receive()
