from kivy.uix.floatlayout import FloatLayout
from PercentageProgress import PercentageProgress
from kivy.lang import Builder

Builder.load_file("kv/percentage_button.kv")

class PercentageButton(FloatLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)

        self.observers = set()
        self.ids.nameLabel.text = text

    def attachObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def setPercentage(self, percentage):
        self.ids.progress.value = round(percentage, 0)