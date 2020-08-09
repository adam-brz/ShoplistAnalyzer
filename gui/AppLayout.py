from ShoppingListGenerator import ShoppingListGenerator
from Options import Options

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from LoadDialog import LoadDialog
from ActionButtonsWidget import ActionButtonsWidget
from LoadDialog import LoadDialog

from ProductListWidget import ProductListWidget

import os

from Product import Product
from Person import Person

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
        self.ids.productList.addProduct(Product("Fasola", 2.30), [Person("A"), Person("B")])
        
    def resultsCallback(self, event):
        pass