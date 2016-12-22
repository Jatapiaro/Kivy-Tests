import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

##Lots of things

class CustomPopup(Popup):
    pass

class SampleBoxLayout(BoxLayout):
    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self,instance,value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox unchecked")

    blue = ObjectProperty(False)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    def switch_on(self,instance,value):
        if value is True:
            print("Switch ON")
        else:
            print("Switch OFF")

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    def spinner_clicked(self,value):
        print("Spinner value: "+value)


class SampleApp(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        return SampleBoxLayout()

sample = SampleApp()
sample.run()