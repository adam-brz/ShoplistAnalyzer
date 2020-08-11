from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from gui.PercentageSelector import PercentageSelector
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/owners_percentage_selector.kv"))

class OwnersPercentageSelector(FloatLayout):
    ok = ObjectProperty(None)
    cancel = ObjectProperty(None)
    layout = ObjectProperty(None)

    def __init__(self, persons, product, **kwargs):
        super().__init__(**kwargs)
        self.product = product
        self.personsSelectors = {}

        for person in persons:
            default_percentage = person.getProductCount(product) * 100
            selector = PercentageSelector(person.name, default_percentage)

            self.layout.add_widget(selector)
            self.personsSelectors[person] = selector

    def okayPressed(self):
        for person, selector in self.personsSelectors.items():
            person.setProductCount(self.product, selector.getPercentage()/100)
        
        self.ok()



    