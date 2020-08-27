from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

from gui.PersonSelector import PersonSelector
from gui.OwnersPercentageSelector import OwnersPercentageSelector

LONG_PRESS_TIME = 1

class PersonSelectionWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selectors = []
        self.product = None

        self._clock = None
        self.rows = 1

    def getPersons(self):
        return [selector.person for selector in self.selectors]

    def setProduct(self, product):
        self.product = product

    def setPersons(self, persons):
        for selector in self.selectors:
            self.remove_widget(selector)

        self.selectors = []
 
        for person in persons:
            self.addPerson(person)

    def addPerson(self, person):
        selector = PersonSelector(person)
        selector.attachObserver(self)
        selector.setPercentage(self.getPersonPart(person) * 100)

        self.add_widget(selector)
        self.selectors.append(selector)

    def update(self, instance, value):
        person = value

        product_count = self.getPersonPart(person)
        owner_count = self.getOwnerCount()

        if product_count and owner_count != 1:
            owner_count -= 1
            self.product.setQuantityForOwner(person, 0)
        elif not product_count:
            owner_count += 1
            self.product.setQuantityForOwner(person, 1.0 / owner_count)

        self.updateCountForOwners(1.0 / owner_count)
        
    def updateCountForOwners(self, newCount):
        for selector in self.selectors:
            owner = selector.person
            if self.getPersonPart(owner):
                self.product.setQuantityForOwner(owner, newCount)
                selector.setPercentage(newCount * 100)
            else:
                selector.setPercentage(0)

    def getOwnerCount(self):
        sum = 0

        for person in self.getPersons():
            if self.getPersonPart(person):
                sum += 1

        return sum

    def getPersonPart(self, person):
        return round(self.product.getQuantityForOwner(person), 3)

    def on_touch_down(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and not self._clock:
            self._clock = Clock.schedule_once(self.askProductOwners, LONG_PRESS_TIME)

        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self._clock:
            self._clock.cancel()
            self._clock = None

        return super().on_touch_up(touch)

    def askProductOwners(self, dt):
        content = OwnersPercentageSelector(self.getPersons(), self.product,
                                          ok = self.setProductOwners,
                                          cancel = self.dismiss_popup)

        self._popup = Popup(title = "Select owners", content = content,
                            size_hint = (0.9, 0.9))
        self._popup.open()

    def setProductOwners(self):
        self.updateSelectors()
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

    def updateSelectors(self):
        for selector in self.selectors:
            person = selector.person
            percentage = self.getPersonPart(person) * 100
            selector.setPercentage(percentage)
