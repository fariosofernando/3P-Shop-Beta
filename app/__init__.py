""" pode-se invocar esse modolo apenas com: from app import nome_do_objecto """


from kivy import animation
from kivy.core import window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from app.view.fonts import fonts
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.clock import Clock
from plugins.widgets.screen_search_and_results import SearchScreen
from plugins.widgets.boxevent import BoxEvent


height_default = None
widget_global = None
h = None # height


class BarraInicial(BoxEvent):
    ...

class Tela(Screen): # tela de pesquisas e apresetancao de resultados da pesquisa.
    def __init__(self, **kw):
        super(Tela, self).__init__(**kw)

    def categoribar_animation(sefl, wid1 = None, widgets = None):

        vazio = []
        for i in widgets.values():
            vazio.append(i)

        animation = Animation(height = dp(130), opacity = 1, transition = "out_elastic") 
        animation_choise = Animation(size = [dp(100), dp(40)], d = .25)
        animation.start(wid1)
        animation_choise.start(vazio[0])
        
        
    def categoribar_animation_disabled(sefl, wid1 = None, widgets = None):
        vazio = []
        for i in widgets.values():
            vazio.append(i)

        animation = Animation(height = dp(0), opacity = 0, d = .25)
        animation_choise = Animation(size = [dp(100), dp(0)], d = .25)
        animation_choise.start(vazio[0])
        animation.start(wid1)

    def back(self):
        
        # esta condição impede que o processo de adição de widgets seja dublicada.
        if widget_global.height == h:
            widget_global.clear_widgets()
            Clock.schedule_once(self.barra_inicial)

    def barra_inicial(self, time):
        initialbar__ = BarraInicial()
        widget_global.add_widget(initialbar__)
        Clock.schedule_once(self.resize)    
    
    def resize(self, time):
        animation = Animation(height = dp(50), d = .1)
        animation.start(widget_global)

Builder.load_file('./app/view/shop.kv')
class ShopPage(Screen):
    def __init__(self, **kw):
        super(ShopPage, self).__init__(**kw)
        Clock.schedule_interval(self.cavando_tamanho, 1 / 30.)
        
    def cavando_tamanho(self, time = None):
        """Já que a altura dos despositivos varia, irei sempre pegar um valor do tamanho de um dos widgets para manipular."""
        
        with open ("screen_size.txt", "w") as file:
            tamanho = self.height
            file.write(str(tamanho))

Builder.load_file('./app/view/home.kv')
class HomePage(Screen):
    def __init__(self, **kw):
        super(HomePage, self).__init__(**kw)
        self.fonts = fonts.Fonts[0]
        Clock.schedule_once(self.cavando_tamanho)

    def cavando_tamanho(self, time = None):
        """Já que a altura dos despositivos varia, irei sempre pegar um valor do tamanho de um dos widgets para manipular."""
        
        with open ("screen_size.txt", "w") as file:
            tamanho = self.height
            file.write(str(tamanho))

    def categoribar_animation(sefl, wid1 = None, widgets = None):

        vazio = []
        for i in widgets.values():
            vazio.append(i)

        animation = Animation(height = dp(130), opacity = 1, transition = "out_elastic") 
        animation_choise = Animation(size = [dp(100), dp(40)], d = .25)
        animation.start(wid1)
        animation_choise.start(vazio[0])
        
        
    def categoribar_animation_disabled(sefl, wid1 = None, widgets = None):
        vazio = []
        for i in widgets.values():
            vazio.append(i)

        animation = Animation(height = dp(0), opacity = 0, d = .25)
        animation_choise = Animation(size = [dp(100), dp(0)], d = .25)
        animation_choise.start(vazio[0])
        animation.start(wid1)


class AppDefaults:
    def __init__(self, value = None, size= None) -> None:
        #self.app_size = Window.size = None# 310,600 if you want to run on pc to encode, use that size.
        self.app_bordeless = Window.borderless = value


class Search(TextInput):
    def __init__(self, **kw):
        super(Search, self).__init__(**kw)
        
        self.multiline = False

    def on_enter(instance, value):
        print('User pressed enter in', instance)


Builder.load_file('./app/view/manager.kv') # Base screen and video manager style
class BasePage(Screen):
    ...
class Manager(ScreenManager):
    font = "/app/view/fonts/segoe/Display.ttf"
    def __init__(self, **kw):
        super(Manager, self).__init__(**kw)

        self.appfont = fonts

        # Screens
        base = BasePage()
        home = HomePage(name = "home")
        shop = ShopPage(name = "shop")
        
        self.add_widget(base)
        self.ids.root_manager.add_widget(home)
        self.ids.root_manager.add_widget(shop)
    
    def cexto_up(self, widget, list_dates = []):

        if list_dates != []:
            print(list_dates)
            widget.image = list_dates[0]
            widget.price = list_dates[1]
            widget.name = list_dates[2]

        new_size = None
        with open ("screen_size.txt", "r") as string_size:
            self.new_size = float(string_size.read())

        global height_default
        animation = Animation(opacity = 1, height = height_default, d = .95, transition = "out_elastic")
        animation.start(widget)

    def cexto_down(self, widget): 
        animation = Animation(opacity = 0, height = dp(0), d = .25)
        animation.start(widget)

    
    def search_shop(self, widget):
        
        # pegando o tamanho compativel com a tela do usuário.
        with open ("screen_size.txt", "r") as string_size:
            self.new_size = float(string_size.read())
            global h
            h = self.new_size
                                     # aqui o self.size é atribuido ao height
        animation = Animation(height = self.new_size, d = .95, transition = "out_elastic")
        animation.start(widget)

        # ao completar a animação ele chama uma funcao que é para adicioanr a Tela ao widget "BarrInicial"
        animation.on_complete(self.animation_search_screen(widget))

    def animation_search_screen(self, widget):
        self.widget = widget
        global widget_global

        widget_global = self.widget # para que a funcao back da class Tela funcione é necesario armazenar este widget a uma variavel para que seja possivel recuperar suas propriedades.
        widget.clear_widgets()

        # e adiciona um novo widget ao "BarraInicial" que é o "Tela"
        Clock.schedule_once(self.add_screen_search)

    def add_screen_search(self, time):
        screen = Tela()
        self.widget.add_widget(screen)


class Shop(MDApp):
    def __init__(self, **kwargs):
        super(Shop, self).__init__(**kwargs)
        Clock.schedule_interval(self.ttt, 1 / 30.)
    
    def ttt(self, time):
        t = self.root.ids.root_manager.get_screen("home").height
        global height_default
        height_default = t

    def build(self):
        return Manager()

# finish