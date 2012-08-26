#!/usr/bin/python
"""
This program is demonstration for face and object detection using haar-like features.
The program finds faces in a camera image or video stream and displays a red box around them.

Original C implementation by:  ?
Python implementation by: Roman Stanchak, James Bowman
"""
import roslib
roslib.load_manifest('opencv_tests') #jk has the dependencies needed

import sys
import os
from optparse import OptionParser

import rospy
import sensor_msgs.msg
from std_msgs.msg import String #jk
from cv_bridge import CvBridge
import cv

# Parameters for haar detection
# From the API:
# The default parameters (scale_factor=2, min_neighbors=3, flags=0) are tuned 
# for accurate yet slow object detection. For a faster operation on real video 
# images the settings are: 
# scale_factor=1.2, min_neighbors=2, flags=CV_HAAR_DO_CANNY_PRUNING, 
# min_size=<minimum possible face size

min_size = (10, 10)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0

#jk
pub = rospy.Publisher('FacesFound', String)
facefound=""

if __name__ == '__main__':

    #jk modified paths to haar file
    haarfile = os.path.join (os.getcwd(), "JTest/haar/haarcascade_frontalface_alt.xml")

    print "HAAR PATH=" + haarfile

    parser = OptionParser(usage = "usage: %prog [options] [filename|camera_index]")
    parser.add_option("-c", "--cascade", action="store", dest="cascade", type="str", help="Haar cascade file, default %default", default = haarfile)
    (options, args) = parser.parse_args()

    cascade = cv.Load(options.cascade)
    br = CvBridge()

    def detect(imgmsg):
        img = br.imgmsg_to_cv(imgmsg, "bgr8")
        # allocate temporary images
        gray = cv.CreateImage((img.width,img.height), 8, 1)
        small_img = cv.CreateImage((cv.Round(img.width / image_scale),
                       cv.Round (img.height / image_scale)), 8, 1)

        # convert color input image to grayscale
        cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

        # scale input image for faster processing
        cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

        cv.EqualizeHist(small_img, small_img)

        if(cascade):
            faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                         haar_scale, min_neighbors, haar_flags, min_size)
            if faces:
	       #jk print face found
	       facefound = "Face Detected!"
               #jk add
               pub.publish(facefound)
	    else:
               facefound = "No Faces Found..."

	print facefound

    rospy.init_node('rosfacedetect')
    image_topic = rospy.resolve_name("image")   
    rospy.Subscriber(image_topic, sensor_msgs.msg.Image, detect)
    rospy.spin()
