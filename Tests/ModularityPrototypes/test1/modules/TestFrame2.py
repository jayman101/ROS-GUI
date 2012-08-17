from ModuleFrame import *

class Frame(ModuleFrame):

    def __init__(self):
        ModuleFrame.__init__(self)

        Button = Gtk.Button(label="Hello from 2")
        Button.show()

        self.frame.put(Button, 100, 10)


