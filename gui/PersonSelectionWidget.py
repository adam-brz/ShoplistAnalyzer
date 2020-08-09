from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

from PersonSelectorWidget import PersonSelectorWidget
from OwnerPercentageSelector import OwnerPercentageSelector

LONG_PRESS_TIME = 1

class PersonSelectionWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.personSelectors = []
        self.persons = []

        self._clock = None
        self.product = None
        self.rows = 1

    def on_touch_down(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and not self._clock:
            self._clock = Clock.schedule_once(self.askProductOwners, LONG_PRESS_TIME)

        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(touch.pos[0], touch.pos[1]) and self._clock:
            self._clock.cancel()
            self._clock = None

        return super().on_touch_up(touch)

    def askProductOwners(self, dt):
        content = OwnerPercentageSelector(self.persons, self.product,
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

    def setProduct(self, product):
        self.product = product

    def getOwnerCount(self):
        sum = 0

        for person in self.persons:
            if self.getPersonPart(person):
                sum += 1

        return sum

    def getPersonPart(self, person):
        return round(person.getProductCount(self.product), 2)

    def update(self, selector, person):
        product_count = self.getPersonPart(person)
        owner_count = self.getOwnerCount()

        if product_count and owner_count != 1:
            owner_count -= 1
            person.setProductCount(self.product, 0)
        elif not product_count:
            owner_count += 1
            person.setProductCount(self.product, 1 / owner_count)

        product_count = 1 / owner_count

        for selector in self.personSelectors:
            owner = selector.person
            if self.getPersonPart(owner):
                owner.setProductCount(self.product, product_count)

            selector.updatePercentage()
    
    def updateSelectors(self):
        for selector in self.personSelectors:
            selector.updatePercentage()

    def setPersons(self, persons):
        for selector in self.personSelectors:
            self.remove_widget(selector)

        self.personSelectors = []
        self.persons = persons
        default_count = 1/len(persons)

        for person in persons:
            person.setProductCount(self.product, default_count)

            selector = PersonSelectorWidget(person, self.product)
            selector.attachObserver(self)
            selector.updatePercentage()

            self.add_widget(selector)
            self.personSelectors.append(selector)
