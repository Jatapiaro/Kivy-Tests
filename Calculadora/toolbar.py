import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampGridLayout(GridLayout):
    pass

class ToolbarApp(App):
    def build(self):
        return SampGridLayout()

samp = ToolbarApp()
samp.run()