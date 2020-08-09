from kivy.uix.gridlayout import GridLayout
from PersonSelectorWidget import PersonSelectorWidget

class PersonSelectionWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.personButtons = []
        self.rows = 1

    def setPersons(self, persons):
        for button in self.personButtons:
            self.remove_widget(button)

        self.personButtons = []

        for person in persons:
            selector = PersonSelectorWidget(person.name)
            selector.setPercentage(round(100/len(persons), 0))

            self.add_widget(selector)
            self.personButtons.append(selector)