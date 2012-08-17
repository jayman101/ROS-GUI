from gi.repository import Gtk
import sys
import os
WINDOWTITLE = "ROS-GUI"

PANELWIDTH = 300
PANELHEIGHT = 200

MAXWIDTH = 1000
MAXHEIGHT = 600

"""
TODO:
Destroy / delete events
Config
"""

class Window():
    index = 0
    def __init__(self):
        self.window = Gtk.Window()
        #self.window.title(WINDOWTITLE)

        # These don't work, the window is autosized anyway? 
        #self.window.set_width(MAXWIDTH)
        #self.window.set_height(MAXHEIGHT)
        
        self.fixedFrame = Gtk.Fixed()
        self.fixedFrame.show()

        self.window.connect("destroy", self.destroy)

        self.window.add(self.fixedFrame)
        self.window.show()

    def destroy(self, window):
        # cleanup should occur here...
        Gtk.main_quit()
        
    def main(self):
        Gtk.main()

    def addFrame(self, frame):
        """ Adds frame or 'panel' with many other controls to main window"""
        # Tiling algorithm could do with some work...
        self.fixedFrame.put(frame, self.index * PANELWIDTH, 0)
        
        self.index += 1

if __name__ == "__main__":
    if sys.argv[-1].lower() == "test1":
        from Test1 import TestFrame
        app = Window()

        test1 = TestFrame("Test 1", "img1.png")
        test2 = TestFrame("Test 2", "img2.png")
        test3 = TestFrame("Test 3", "img1.png")

        app.addFrame(test1.frame)
        app.addFrame(test2.frame)
        app.addFrame(test3.frame)
    
        app.main()
    

    if sys.argv[-1].lower() == "test2":
        ########################################
        # Begin bad idea code.
        app = Window()
        
        os.chdir("./modules")
        # todo: os.system is depricated, too lazy to google alternative
        os.system("python generateImport.py")
	
        sys.path.append(os.getcwd())
        
        import ModuleObjects
        for obj in ModuleObjects.modules:
            objFrameInstance = obj.Frame()
            
            app.addFrame(objFrameInstance.frame)

        app.main()
        # End bad idea code
        ########################################
    else:
        print("Usage: engine.py TEST\n")
        print("test1: An example of tiling")
        print("test2: External module hack / test")
        
        
