# CRIANDO A APLICAÇÃO "HELLO WORLD"

from kivy.app import App
from kivy.uix.label import Label

def build():
    return Label(text = "Helllo World!")

hello_world = App()
hello_world.build = build
hello_world.run()
