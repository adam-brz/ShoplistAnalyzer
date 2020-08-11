from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/load_dialog.kv"))

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)