from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from PersonSelectionWidget import PersonSelectionWidget

Builder.load_file("kv/product_entry.kv")

class ProductEntryWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product = None
        self.selectionWidget = self.ids.selection_widget

    def setProduct(self, product):
        self.product = product
        self.setName(product.name)
        self.setPrice(product.price)

    def setName(self, name):
        self.ids.product_name.text = name

    def setPrice(self, price):
        self.ids.product_price.text = str(price)

    def setOwners(self, owners):
        self.selectionWidget.setPersons(owners)