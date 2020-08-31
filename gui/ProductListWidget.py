from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from gui.ProductEntryWidget import ProductEntryWidget
from ShoppingList import ShoppingList
from Observer import Observer

from OwnerGroup import OwnerGroupFactory
from OwnerInfo import OwnerInfoFactory

import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "kv/product_list.kv"))

class ProductListWidget(FloatLayout, Observer):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entry_widgets = []
        self.shoppingList = ShoppingList()
        self.expectedSum = 0

    def update(self, instance, value):
        self.notify(instance, value)

    def addShoppingList(self, shoppingList):
        self.shoppingList.merge(shoppingList)

        for product in shoppingList.getProducts():
            self.__addProductWidget(product)

        self.expectedSum += shoppingList.realSum

    def addProduct(self, product):
        self.shoppingList.addProduct(product)
        self.__addProductWidget(product)
        self.notify(self, product)

    def __addProductWidget(self, product):
        new_entry = ProductEntryWidget()

        new_entry.setProduct(product)
        new_entry.setOwners(product.getOwners())
        new_entry.attachObserver(self)

        self.entry_widgets.append(new_entry)
        self.layout.add_widget(new_entry)

    def removeProduct(self, product):
        for widget in self.entry_widgets:
            if widget.getProduct() == product:
                self.layout.remove_widget(widget)
                self.entry_widgets.remove(widget)
                self.shoppingList.removeProduct(product)
                self.notify(self, None)
  
    def clear(self):
        self.shoppingList.clear()
        self.expectedSum = 0
        
        for widget in self.entry_widgets:
            self.layout.remove_widget(widget)

        self.entry_widgets = []

        OwnerGroupFactory().clear()
        OwnerInfoFactory().clear()

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