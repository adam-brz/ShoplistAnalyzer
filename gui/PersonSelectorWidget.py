from kivy.uix.floatlayout import FloatLayout
from PercentageProgress import PercentageProgress
from kivy.lang import Builder

Builder.load_file("kv/person_selector.kv")

class PersonSelectorWidget(FloatLayout):
    def __init__(self, person, product, **kwargs):
        super().__init__(**kwargs)

        self.person = person
        self.product = product
        self.observers = set()

        self.ids.nameLabel.text = person.name

    def attachObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self, self.person)

    def updatePercentage(self):
        percentage = self.person.getProductCount(self.product) * 100
        self.ids.progress.value = round(percentage, 0)