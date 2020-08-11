from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/action_buttons.kv"))

class ActionButtonsWidget(FloatLayout):
    pass