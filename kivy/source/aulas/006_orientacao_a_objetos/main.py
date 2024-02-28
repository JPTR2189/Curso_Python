from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput


class MeuPrograma(App):

    Window.size = 525, 600
    def click(self):
        global ed
        print(ed.text)
    def build(self):

        layout = FloatLayout()
        global ed

        ed = TextInput(text="eXcript")
        ed.size_hint = None, None
        ed.height = 300
        ed.width = 400
        ed.x = 60
        ed.y = 250

        bt = Button(text="Clique aqui")
        bt.on_press = self.click
        bt.size_hint = None, None
        bt.width = 200
        bt.height = 50
        bt.y = 150
        bt.x = 160

        layout.add_widget(ed)
        layout.add_widget(bt)

        return layout


app = MeuPrograma()
app.run()
app.title = "eXcript"
