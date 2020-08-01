# -*- coding: UTF-8 -*-

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from AppEventDispatcher import AppEventDispatcher


class AppLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.actionButtons.ids.button_generate.bind(on_release = self.parseFileCallback)
        event_dispatcher = AppEventDispatcher()
        event_dispatcher.bind(on_generate = self.parseFileCallback)
        event_dispatcher.bind(on_clear = self.clearCallback)
        event_dispatcher.bind(on_options = self.optionsCallback)
        event_dispatcher.bind(on_results = self.resultsCallback)

    def parseFileCallback(self, *args):
        print(self.ids.file_input.text)

    def clearCallback(self, *args):
        pass

    def optionsCallback(self, *args):
        pass

    def resultsCallback(self, *args):
        pass

class ActionButtonsWidget(FloatLayout):
    def generatePressed(self):
        AppEventDispatcher().dispatch("on_generate")

    def clearPressed(self):
        AppEventDispatcher().dispatch("on_clear")

    def optionsPressed(self):
        AppEventDispatcher().dispatch("on_options")

    def resultsPressed(self):
        AppEventDispatcher().dispatch("on_results")

class ProductListWidget(FloatLayout):
    pass

class ProductEntryWidget(GridLayout):
    pass

class PersonSelectionWidget(GridLayout):
    pass

class Application(App):
    def build(self):
        return AppLayout()