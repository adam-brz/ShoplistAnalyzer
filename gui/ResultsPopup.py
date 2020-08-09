from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

Builder.load_file("kv/results_popup.kv")

class ResultsPopup(FloatLayout):
    cancel = ObjectProperty(None)
    text = StringProperty("")
