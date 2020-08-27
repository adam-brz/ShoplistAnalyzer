from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from gui.PersonSelectionWidget import PersonSelectionWidget
from Observer import Observer
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/product_entry.kv"))

class ProductEntryWidget(GridLayout, Observer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product = None
        self.selectionWidget = self.ids.selection_widget

        self.attachObserver(self)
        self.ids.product_price.bind(text = self.notify)
        self.ids.product_price.bind(focus = self.validateText)

    def update(self, instance, value):
        try:
            value = float(value.replace(",", "."))
        except ValueError:
            value = 0

        self.product.price = value

    def validateText(self, instance, value):
        if not value:
            self.setPrice(self.product.price)

    def getProduct(self):
        return self.product

    def setProduct(self, product):
        self.product = product
        self.selectionWidget.setProduct(product)
        
        self.setName(product.name)
        self.setPrice(product.price)

    def setName(self, name):
        self.ids.product_name.text = name

    def setPrice(self, price):
        self.ids.product_price.text = "{0:.2f}".format(price)

    def setOwners(self, owners):
        self.selectionWidget.setPersons(owners)