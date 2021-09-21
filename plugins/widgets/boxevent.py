""" BoxLayout com eventos de um butão. """

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder


Builder.load_file("./plugins/widgets/boxevent.kv")
class BoxEvent(BoxLayout, Button):
    def __init__(self, **kwargs):
        super(BoxEvent, self).__init__(**kwargs)

        #  remove button design
        self.background_normal = ""
        self.background_down =  ""
        self.background_color = (0, 0, 0, 0)

