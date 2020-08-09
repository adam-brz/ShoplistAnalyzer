from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

Builder.load_file("kv/results.kv")

class ResultsWidget(FloatLayout):
    cancel = ObjectProperty(None)
    text = StringProperty("")
