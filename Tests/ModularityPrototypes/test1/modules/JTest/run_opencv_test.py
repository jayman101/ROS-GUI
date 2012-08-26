#!/usr/bin/env python
import roslib
#roslib.load_manifest('opencv_tests')

import os
import sys
import rospy

camera_topic = ""
py_file = ""

def run_face_recog():

	test_dir = roslib.packages.get_pkg_dir("opencv_tests")
	print "TEST DIR=" + test_dir
	py_file = os.path.join(test_dir,"nodes/")
	print "PY FILE=" + py_file
    	print "Running file with args:" + camera_topic
    	os.system(py_file + "rosfacedetect.py" + camera_topic)

	print "Python file path=" + py_file

if __name__ == "__main__":
    if len(sys.argv) == 2:	
	camera_topic = " " + sys.argv[1]
        print "ARG 1 IS:" + camera_topic
    else:
        print usage()
        sys.exit(1)

    run_face_recog()

