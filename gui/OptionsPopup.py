from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("kv/options_popup.kv")

class OptionsPopup(FloatLayout):
    cancel = ObjectProperty(None)

    def __init__(self, options, **kwargs):
        super().__init__(**kwargs)
        self.options = options
        self.ids.optionsInput.text = options.getPersonsString()

    def saveOptions(self):
        self.options.setPersonsFromString(self.ids.optionsInput.text)
        self.options.save()
        self.cancel()
