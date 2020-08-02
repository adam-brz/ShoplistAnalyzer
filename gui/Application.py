# -*- coding: UTF-8 -*-

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

import os
from ShoppingListGenerator import ShoppingListGenerator
from Options import Options

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class AppLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.options = Options()

        buttons = self.ids.actionButtons.ids
        buttons.button_generate.bind(on_release = self.parseFileCallback)
        buttons.button_clear.bind(on_release = self.clearCallback)
        buttons.button_options.bind(on_release = self.optionsCallback)
        buttons.button_results.bind(on_release = self.resultsCallback)

    def selectFile(self):
        content = LoadDialog(load=self.getFilename, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def getFilename(self, path, filename):
        self.ids.file_input.text = os.path.join(path, filename[0])
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

    def parseFileCallback(self, event):
        imageFile = self.ids.file_input.text.strip()

        if not imageFile:
            return

        person_names = self.options.getPersons()
        generator = ShoppingListGenerator(person_names)
        shoppingList = generator.generateFromImage(imageFile)
    
        self.ids.productList.addShoppingList(shoppingList)

    def clearCallback(self, event):
        self.ids.productList.clear()

    def optionsCallback(self, event):
        pass

    def resultsCallback(self, event):
        pass

class ActionButtonsWidget(FloatLayout):
    pass

class ProductListWidget(FloatLayout):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entry_widgets = []
        self.shoppingLists = []

    def addShoppingList(self, shoppingList):
        self.shoppingLists.append(shoppingList)

        for product in shoppingList.getProducts():
            self.addProduct(product, shoppingList.persons)

    def addProduct(self, product, owners):
        new_entry = ProductEntryWidget()
        new_entry.setProduct(product)
        new_entry.setOwners(owners)

        self.entry_widgets.append(new_entry)
        self.layout.add_widget(new_entry)
  
    def clear(self):
        self.shoppingLists = []
        for widget in self.entry_widgets:
            self.layout.remove_widget(widget)

        self.entry_widgets = []

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

class PersonSelectionWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.personButtons = []

    def setPersons(self, persons):
        for button in self.personButtons:
            self.remove_widget(button)

        self.personButtons = []

        for person in persons:
            button = Button(text = person.name)
            self.add_widget(button)
            self.personButtons.append(button)

class Application(App):
    def build(self):
        return AppLayout()