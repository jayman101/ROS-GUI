#!/usr/bin/env python
import roslib
roslib.load_manifest('pythonsrv')

from pythonsrv.srv import *
import rospy

from std_msgs.msg import String

subscribe_to_topic = ""

def callback(data):
	rospy.loginfo("Data Recieved=%s",data.data)

def subscriber():
	rospy.init_node("subscriber",anonymous=True)
	rospy.Subscriber(subscribe_to_topic, String, callback)
	rospy.spin()

if __name__ == "__main__":
    if len(sys.argv) == 2:
	subscribe_to_topic = sys.argv[1]
        print "Subscribing to topic:" + subscribe_to_topic
    else:
        print usage()
        sys.exit(1)

    subscriber()
