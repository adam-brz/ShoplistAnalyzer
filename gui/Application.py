# -*- coding: UTF-8 -*-

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

class AppLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        buttons = self.ids.actionButtons.ids
        buttons.button_generate.bind(on_release = self.parseFileCallback)
        buttons.button_clear.bind(on_release = self.clearCallback)
        buttons.button_options.bind(on_release = self.optionsCallback)
        buttons.button_results.bind(on_release = self.resultsCallback)

    def selectFile(self):
        print("Works")

    def parseFileCallback(self, event):
        print(self.ids.file_input.text)

    def clearCallback(self, event):
        pass

    def optionsCallback(self, event):
        pass

    def resultsCallback(self, event):
        pass

class ActionButtonsWidget(FloatLayout):
    pass

class ProductListWidget(FloatLayout):
    pass

class ProductEntryWidget(GridLayout):
    pass

class PersonSelectionWidget(GridLayout):
    pass

class Application(App):
    def build(self):
        return AppLayout()