from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from gui.PercentageProgress import PercentageProgress

import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/percentage_button.kv"))

class PercentageButton(FloatLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.ids.nameLabel.text = text

    def setPercentage(self, percentage):
        self.ids.progress.value = round(percentage, 0)

    def buttonPressed(self):
        pass