from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/percentage_selector.kv"))

class PercentageSelector(GridLayout):
    slider = ObjectProperty(None)

    def __init__(self, text, default_value = 0, **kwargs):
        super().__init__(**kwargs)
        self.ids.labelName.text = text
        self.slider.value = default_value

    def getPercentage(self):
        return self.slider.value