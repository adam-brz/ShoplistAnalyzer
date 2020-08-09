from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder

Builder.load_file("kv/percentage_progress.kv")

class PercentageProgress(FloatLayout):
    value = NumericProperty()