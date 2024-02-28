from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    global ed
    print(ed.text)
def build():

    layout = FloatLayout()

    global ed
    ed = TextInput(text="eXcript")
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250


    bt = Button(text="Clique aqui")
    bt.on_press = click
    bt.size_hint = None, None
    bt.width = 200
    bt.height = 50
    bt.y = 150
    bt.x = 160

    bt.on_press = click


    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout



janela = App()
janela.title = "eXcript"

from kivy.core.window import Window

Window.size = 525, 600
janela.build = build
janela.run()