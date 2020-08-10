from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

from PercentageButton import PercentageButton
from OwnersPercentageSelector import OwnersPercentageSelector

LONG_PRESS_TIME = 1

class PersonSelectionWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selectorPerson = {}
        self.product = None

        self._clock = None
        self.rows = 1

    def getPersons(self):
        return self.selectorPerson.values()

    def setProduct(self, product):
        self.product = product

    def setPersons(self, persons):
        for selector in self.selectorPerson:
            self.remove_widget(selector)

        self.selectorPerson = {}
        default_count = 1/len(persons)

        for person in persons:
            person.setProductCount(self.product, default_count)

            selector = PercentageButton(person.name)
            selector.attachObserver(self)
            selector.setPercentage(default_count * 100)

            self.add_widget(selector)
            self.selectorPerson[selector] = person

    def update(self, selector):
        person = self.selectorPerson[selector]

        product_count = self.getPersonPart(person)
        owner_count = self.getOwnerCount()

        if product_count and owner_count != 1:
            owner_count -= 1
            person.setProductCount(self.product, 0)
        elif not product_count:
            owner_count += 1
            person.setProductCount(self.product, 1 / owner_count)

        product_count = 1 / owner_count

        for selector in self.selectorPerson:
            owner = self.selectorPerson[selector]
            if self.getPersonPart(owner):
                owner.setProductCount(self.product, product_count)
                selector.setPercentage(product_count * 100)
            else:
                selector.setPercentage(0)

    def getOwnerCount(self):
        sum = 0

        for person in self.getPersons():
            if self.getPersonPart(person):
                sum += 1

        return sum

    def getPersonPart(self, person):
        return round(person.getProductCount(self.product), 3)

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
        for selector in self.selectorPerson:
            person = self.selectorPerson[selector]
            percentage = person.getProductCount(self.product) * 100
            selector.setPercentage(percentage)
