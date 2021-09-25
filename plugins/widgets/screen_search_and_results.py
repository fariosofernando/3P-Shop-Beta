""" Tela de buscas e resulatados. """

# python

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""

<SearchScreen>:
    BoxLayout: 
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: "40dp"
            padding: "22dp", "0dp"
            TextInput:
                hint_text: "Esolha o seu tamanho"
                cursor_color: .2, .2, .2, 1
                hint_text_color: [.8, .8, .8, .5]
                background_normal: "./app/view/img/textfield.png"
                background_active: "./app/view/img/textfield_down.png"
                padding_x: "15dp"
                padding_y: "8dp"
                font_size: "18sp"
        widget:
""")
class SearchScreen(Screen):
    ...