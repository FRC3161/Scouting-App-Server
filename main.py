import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button

from Scan import Scan
from TBA import TBA
from Verify import Verify

kivy.require('1.11.1')

class Odin(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scan = Scan("data.csv")

    def build(self):
        return  MainScreen(self.scan)

    def on_request_close(self, *args):
        self.scan.cleanup()
        return True

class MainScreen(RelativeLayout):

    def __init__(self, scan, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)

        self.cols = 1
        self.scan = scan

        super(MainScreen, self).__init__(**kwargs)

        self.add_widget(Label(text="Odin", font_size='48', pos=(0, 200), color=[0, 0, 0, 1], font_name='Rajdhani-Bold.ttf'))

        self.scan_button = Button(text="Scan", size=(120, 50), size_hint=(None, None), pos=(348, 350))
        self.scan_button.bind(on_press=self.scan_onpress)
        self.add_widget(self.scan_button)

    def scan_onpress(self, instance):
        self.scan.scan()

tba = TBA('2020onosh')
Odin().run()