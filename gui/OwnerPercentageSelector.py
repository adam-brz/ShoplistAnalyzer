from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("kv/owner_percentage_selector.kv")

class OwnerPercentageSelector(FloatLayout):
    ok = ObjectProperty(None)
    cancel = ObjectProperty(None)
    layout = ObjectProperty(None)

    def __init__(self, persons, product, **kwargs):
        super().__init__(**kwargs)
        self.persons = persons
        self.product = product
        self.selectors = []

        for person in persons:
            percentage = person.getProductCount(product) * 100
            selector = PercentageSelector(person, percentage)

            self.layout.add_widget(selector)
            self.selectors.append(selector)

    def okayPressed(self):
        for selector in self.selectors:
            selector.person.setProductCount(self.product, selector.getPercentage()/100)
        
        self.ok()

class PercentageSelector(GridLayout):
    slider = ObjectProperty(None)

    def __init__(self, person, percentage, **kwargs):
        super().__init__(**kwargs)
        self.person = person
        self.ids.labelName.text = person.name
        self.slider.value = percentage

    def getPercentage(self):
        return self.slider.value

    