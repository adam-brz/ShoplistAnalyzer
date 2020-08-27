from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from gui.ProductEntryWidget import ProductEntryWidget
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/product_list.kv"))

class ProductListWidget(FloatLayout):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entry_widgets = []
        self.shoppingList = None

        self.expectedSum = 0

    def attachObserver(self, observer):
        for entry in self.entry_widgets:
            entry.attachObserver(observer)

    def removeObserver(self, observer):
        for entry in self.entry_widgets:
            entry.removeObserver(observer)

    def addShoppingList(self, shoppingList):
        if not self.shoppingList:
            self.shoppingList = shoppingList
        else:
            self.shoppingList.merge(shoppingList)

        for product in shoppingList.getProducts():
            self.__addProduct(product)

        self.expectedSum += shoppingList.realSum

    def __addProduct(self, product):
        new_entry = ProductEntryWidget()
        new_entry.setProduct(product)
        new_entry.setOwners(product.getOwners())

        self.entry_widgets.append(new_entry)
        self.layout.add_widget(new_entry)
  
    def clear(self):
        self.shoppingList.clear()
        self.expectedSum = 0
        
        for widget in self.entry_widgets:
            self.layout.remove_widget(widget)

        self.entry_widgets = []

    def getTotalSum(self):
        return self.shoppingList.getTotalSum()

    def getRealSum(self):
        return self.expectedSum

    def getBill(self):
        bill = self.shoppingList.generateBill()
        compactBill = {}

        for person in bill:
            if not person.name in compactBill:
                compactBill[person.name] = bill[person]
            else:
                compactBill[person.name] += bill[person]

        return compactBill