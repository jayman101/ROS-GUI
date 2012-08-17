from gi.repository import Gtk
""" Objects for engine.py test1 """

class ModuleFrame():

    def __init__(self):
        self.frame = Gtk.Fixed()
        self.frame.show()

class TestFrame(ModuleFrame):

    def __init__(self, SomeText, img):
        ModuleFrame.__init__(self)

        BgImage = Gtk.Image()
        BgImage.set_from_file(img)
        BgImage.show()
        # Ok, so cheating a little bit, img is 300x200.
        # I'm confident that framesize isn't dynamic though..
        self.frame.put(BgImage, 0, 0)

        Button = Gtk.Button(label=SomeText)
        Button.show()

        self.frame.put(Button, 100, 10)



