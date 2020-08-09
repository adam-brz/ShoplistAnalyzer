from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from ProductListWidget import ProductListWidget
from ActionButtonsWidget import ActionButtonsWidget
from ResultsPopup import ResultsPopup
from LoadDialog import LoadDialog

from ShoppingListGenerator import ShoppingListGenerator
from Options import Options
import os

class AppLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._popup = None
        self.options = Options()

        buttons = self.ids.actionButtons.ids
        buttons.button_generate.bind(on_release = self.parseFileCallback)
        buttons.button_clear.bind(on_release = self.clearCallback)
        buttons.button_options.bind(on_release = self.optionsCallback)
        buttons.button_results.bind(on_release = self.resultsCallback)

    def loadFilePopup(self):
        content = LoadDialog(load = self.__getFilename, cancel = self.dismiss_popup)
        self._popup = Popup(title = "Load file", content = content,
                            size_hint = (0.9, 0.9))
        self._popup.open()

    def __getFilename(self, path, filename):
        self.ids.file_input.text = os.path.join(path, filename[0])
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

    def parseFileCallback(self, event):
        filename = self.ids.file_input.text.strip()

        if not filename:
            return

        person_names = self.options.getPersons()
        generator = ShoppingListGenerator(person_names)
        shoppingList = generator.generateFromImage(filename)
    
        self.ids.productList.addShoppingList(shoppingList)

    def clearCallback(self, event):
        self.ids.productList.clear()

    def optionsCallback(self, event):
        pass
        
    def resultsCallback(self, event):
        content = ResultsPopup(cancel = self.dismiss_popup)
        content.text = "\n".join("{0} = {1:.2f}".format(person, sum) for person,sum
                                     in self.ids.productList.getBill().items())

        if not content.text:
            content.text = "No Results"

        self._popup = Popup(title = "Results", content = content,
                            size_hint = (0.9, 0.9))
        self._popup.open()