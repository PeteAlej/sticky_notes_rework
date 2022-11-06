# Prueba 1 de reconstruir el MS Sticky Notes con mis toques.
# Posiblemente requiera de kivy y un virtual environment diferente.

from distutils.command.config import config
import kivy
from kivy.config import Config

# El Config.set siempre se debe llevar a cabo antes de cualquier otro import para evitar que estos sobreescriban la config de la ventana.
# Por alguna razón, si se hace load el modulo de Window ANTES de hacer las configs, se ignoran algunas Config.

window_width = ['graphics', 'width', '400'] # Valores para configurar el ancho de la ventana inicial.
window_height = ['graphics', 'height', '600']   # Valores para configura el alto de la ventana inicial.

Config.set(window_height[0], window_height[1], window_height[2])    # Setear el alto de la ventana inicial.
Config.set(window_width[0], window_width[1], window_width[2])   # Setear el ancho de la ventana inicial.
Config.set('graphics', 'resizable', True)   # Permitir que el tamaño de la ventana se pueda modificar.
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

import time
import subprocess
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Canvas
from kivy.core.text.markup import *
from kivy.lang import Builder


window_size_min = [300, 400]
Window.minimum_width = window_size_min[0]
Window.minimum_height = window_size_min[1]


# Window.size = (250, 300)

# Builder.load_file('stickyNotes_float.kv')
Builder.load_file('homeWindow.kv')
Builder.load_file('notesWindow.kv')

class homeWindow(Widget):
    
    def resetSearch(self):
        searchTerm = self.ids.padSearchBar.text
        if "Search..." in searchTerm:
            self.ids.padSearchBar.text = ""
        elif searchTerm != "Search..." and searchTerm != "":
            pass
        elif searchTerm != "Search..." or searchTerm == "":
            self.ids.padSearchBar.text = "Search..."
    
    def searchPad(self, text):
        print(text)
    
    def createNewPad(self, *args):
        numNotes = len(self.ids.notesList.children)
        button = Button(
            text = f"Label {numNotes+1}",
            text_size = self.size,
            font_name = "Framd",
            font_size = 24,
        )
        self.ids.notesList.add_widget(button)
    

class notesWindow(Widget):
    pass

class StickyPadApp(App):
    
    def build(self):
        # return Label(text='Hello world')  
        for i in range(10):
            btn = Button(
                text = str(i),
                #size_hint_y = None,
                #height = 30,
                #size_x = Window.width
            )
            notesList = homeWindow().ids.notesList.add_widget(btn)
        
        return homeWindow();


if __name__ == '__main__':
    StickyPadApp().run()
