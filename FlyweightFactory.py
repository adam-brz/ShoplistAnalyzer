# -*- coding : UTF-8 -*-

class FlyweightFactory:
    _instance = None

    def __new__(self, cls):
        if not cls._instance:
            cls._instance = super().__new__(self)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.flyweights = []

    def _addFlyweight(self, flyweight):
        if not flyweight in self.flyweights:
            self.flyweights.append(flyweight)

    def remove(self, item):
        self.flyweights.remove(item)