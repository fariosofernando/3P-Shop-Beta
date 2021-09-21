"""uix.Widget Cexto. Serve para conter os dados de um certo produto."""

# python


from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file("./plugins/widgets/cexto.kv")
class Cexto(BoxLayout):
    font = "/app/view/fonts/segoe/Display.ttf"

