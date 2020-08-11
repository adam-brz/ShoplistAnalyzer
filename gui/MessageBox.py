from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/message_box.kv"))

class MessageBox(FloatLayout):
    ok = ObjectProperty(None)
    text = StringProperty("")
