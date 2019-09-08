#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def transmit():
    pub = rospy.Publisher('jain', Int32, queue_size=10)
    rospy.init_node('transmit', anonymous=True)
    rate = rospy.Rate(20)
    k = 2
    n = 4
    while not rospy.is_shutdown():
        k = k + n
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        transmit()
    except rospy.ROSInterruptException:
        pass
