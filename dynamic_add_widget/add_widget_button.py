# Testing for adding a widget with the press of a button.

from distutils.command.config import config
import kivy
from kivy.config import Config

window_width = ['graphics', 'width', '400'] # Valores para configurar el ancho de la ventana inicial.
window_height = ['graphics', 'height', '600']   # Valores para configura el alto de la ventana inicial.

Config.set(window_height[0], window_height[1], window_height[2])    # Setear el alto de la ventana inicial.
Config.set(window_width[0], window_width[1], window_width[2])   # Setear el ancho de la ventana inicial.
Config.set('graphics', 'resizable', True)   # Permitir que el tamaño de la ventana se pueda modificar.
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
import threading
import sqlite3 as lite
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.text.markup import *
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('add_widget_button.kv')

class new_widget(BoxLayout):
    pass

class baseboard(Screen):
    
    def __init__(self, **kwargs):
        super(baseboard, self).__init__(**kwargs)
    
    def add_custom_widget(self):
        custom_widget = new_widget()
        self.ids.container.add_widget(custom_widget)
        print(self.ids.container.height)
        #new_entry = self.ids.container
        #self.ids.scroll.add_widget(self.ids.container)

class add_widget_button(App):
    def build(self):
        return baseboard()


if __name__ == '__main__':
    add_widget_button().run()