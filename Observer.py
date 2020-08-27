# -*- coding : UTF-8 -*-

class Observer:
    def __init__(self):
        self.observers = set()

    def attachObserver(self, observer):
        self.observers.add(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notify(self, instance, value):
        for observer in self.observers:
            observer.update(instance, value)

    def update(self, instance, value):
        raise NotImplementedError