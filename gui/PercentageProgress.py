from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/percentage_progress.kv"))

class PercentageProgress(FloatLayout):
    value = NumericProperty()