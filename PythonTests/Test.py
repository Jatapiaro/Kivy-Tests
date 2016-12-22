from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import Graph, MeshLinePlot
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas
from kivy.utils import get_color_from_hex as rgb
from numpy import sin


kv = """
<GraphCustom>:
<Test>:
    orientation: 'vertical'
    GraphCustom:
		size: self.parent.size
		pos: self.parent.pos
"""

Builder.load_string(kv)

class GraphCustom(Graph):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_options = {'color': rgb('#FF0000'), 'bold': True}
        self.background_color = rgb('f8f8f2')
        self.tick_color = rgb('808080')
        self.border_color = rgb('808080')
        self.xlabel = 'X'
        self.ylabel = 'Y'
        self.y_grid_label = True
        self.x_grid_label = True
        self.padding = 5
        self.x_grid = True
        self.y_grid = True
        self.xmin = -0
        self.xmax = 100
        self.ymin = -1
        self.ymax = 1
        self.stop = False
        self.plot = MeshLinePlot(color=[0, 0, 0.75, 1])
        self.plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        self.add_plot(self.plot)

class Test(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        wid = FigureCanvas(fig1)
        self.add_widget(wid)

class TestApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    TestApp().run()
