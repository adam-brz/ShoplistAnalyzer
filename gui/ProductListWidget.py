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
        self.shoppingLists = []

        self.expectedSum = 0

    def attachObserver(self, observer):
        for entry in self.entry_widgets:
            entry.attachObserver(observer)

    def removeObserver(self, observer):
        for entry in self.entry_widgets:
            entry.removeObserver(observer)

    def addShoppingList(self, shoppingList):
        self.shoppingLists.append(shoppingList)

        for product in shoppingList.getProducts():
            self.__addProduct(product, shoppingList.persons)

        self.expectedSum += shoppingList.realSum

    def __addProduct(self, product, owners):
        new_entry = ProductEntryWidget()
        new_entry.setProduct(product)
        new_entry.setOwners(owners)

        self.entry_widgets.append(new_entry)
        self.layout.add_widget(new_entry)
  
    def clear(self):
        self.shoppingLists = []
        self.expectedSum = 0
        
        for widget in self.entry_widgets:
            self.layout.remove_widget(widget)

        self.entry_widgets = []

    def getTotalSum(self):
        return sum(shop_list.getTotalSum() for shop_list in self.shoppingLists)

    def getRealSum(self):
        return self.expectedSum

    def getBill(self):
        sum = {}
        for shop_list in self.shoppingLists:
            sum = self.__sumDicts(sum, shop_list.generateBill())

        return sum

    def __sumDicts(self, a, b):
        for key in b.keys():
            if key in a.keys():
                a[key] += b[key]
            else:
                a[key] = b[key]
        return a