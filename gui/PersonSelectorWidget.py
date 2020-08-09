from kivy.uix.floatlayout import FloatLayout
from PercentageProgress import PercentageProgress
from kivy.lang import Builder

Builder.load_file("kv/person_selector.kv")

class PersonSelectorWidget(FloatLayout):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.ids.selectorText.text = name

    def setPercentage(self, percentage):
        self.ids.progress.value = percentage