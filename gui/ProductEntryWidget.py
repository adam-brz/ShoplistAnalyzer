from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from PersonSelectionWidget import PersonSelectionWidget

Builder.load_file("kv/product_entry.kv")

def on_text(instance, value):
    print('The widget', instance, 'have:', value)

class ProductEntryWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.observers = set()
        self.product = None
        self.selectionWidget = self.ids.selection_widget

        self.attachObserver(self)
        self.ids.product_price.bind(text = self.notify)
        self.ids.product_price.bind(focus = self.validateText)
        
    def attachObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def update(self, instance, value):
        try:
            value = float(value.replace(",", "."))
        except ValueError:
            value = 0

        self.product.price = value

    def validateText(self, instance, value):
        if not value:
            self.setPrice(self.product.price)

    def notify(self, instance, value):
        for observer in self.observers:
            observer.update(instance, value)

    def setProduct(self, product):
        self.product = product
        self.setName(product.name)
        self.setPrice(product.price)

    def setName(self, name):
        self.ids.product_name.text = name

    def setPrice(self, price):
        self.ids.product_price.text = "{0:.2f}".format(price)

    def setOwners(self, owners):
        self.selectionWidget.setPersons(owners)