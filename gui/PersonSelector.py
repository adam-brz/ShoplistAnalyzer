from gui.PercentageButton import PercentageButton
from Observer import Observer

class PersonSelector(PercentageButton, Observer):
    def __init__(self, person, **kwargs):
        super().__init__(person.name, **kwargs)
        self.person = person

    def buttonPressed(self):
        self.notify(self, self.person)