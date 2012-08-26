from ModuleFrame import *

import os

class Frame(ModuleFrame):

    def __init__(self):
        ModuleFrame.__init__(self)

        Button = Gtk.Button(label="   OpenCV Tests   ")
        Button.show()

        Button.connect("clicked", self.cvtest_clicked)
        self.frame.put(Button, 0, 20)
	#

	#jk custom modification of rosfacedetect.py with correct path to haar xml file
        Button2 = Gtk.Button(label="OpenCV Face Detect")
        Button2.show()

        Button2.connect("clicked", self.face_detect_clicked)
        self.frame.put(Button2, 0, 60)
	#
        Button3 = Gtk.Button(label="Subscribe to topic")
        Button3.show()

        Button3.connect("clicked", self.subscribe_clicked)
        self.frame.put(Button3, 0, 100)
	#
	statusNameLabel = Gtk.Label("Subscriber Status:")
	statusNameLabel.show()
	self.frame.put(statusNameLabel, 0, 140)
	#
	statusLabel = Gtk.Label("SOLVED")
	statusLabel.show()
	self.frame.put(statusLabel, 0, 160)

    #jk - this will attmpt to run the face detection from the opencv_tests pkg - currently there is an issue with the haar xml path
    def cvtest_clicked(self, Button):
           print "Clicked OpenCV test button 1"
           os.system("JTest/run_opencv_test.py image:=/usb_cam/image_raw")
	
    #jk - this will run a customized face detect py file
    def face_detect_clicked(self, Button2):
           print "Clicked OpenCV test button 2"
           os.system("JTest/rosfacedetect.py image:=/usb_cam/image_raw")
	   #jk - rosrun alternate
	   #os.system("rosrun pythonsrv rosfacedetect.py image:=/usb_cam/image_raw")

    #jk subscribe to specific topic and recieve a string message
    def subscribe_clicked(self, Button3):
           print "Clicked subscribe button"
           os.system("JTest/subscriber.py FacesFound")

