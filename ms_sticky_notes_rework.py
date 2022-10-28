# Prueba 1 de reconstruir el MS Sticky Notes con mis toques.
# Posiblemente requiera de kivy y un virtual environment diferente.

from distutils.command.config import config
import kivy
from kivy.config import Config

# El Config.set siempre se debe llevar a cabo antes de cualquier otro import para evitar que estos sobreescriban la config de la ventana.

window_width = ['graphics', 'width', '300']
window_height = ['graphics', 'height', '400']

Config.set(window_width[0], window_width[1], window_width[2])
Config.set(window_height[0], window_height[1], window_height[2])
Config.set('graphics', 'resizable', True)

import time
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Window.size = (250, 300)

Builder.load_file('stickyNotes.kv')

class myLayout(Widget):
        pass

class MyApp(App):
    
    def build(self):
        # return Label(text='Hello world')
        return myLayout();

if __name__ == '__main__':
    MyApp().run()
