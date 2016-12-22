import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])

class CalcGridLayout(GridLayout):

    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except:
                self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()