# -*- coding : UTF-8 -*-

from FlyweightFactory import FlyweightFactory

class OwnerInfoFactory(FlyweightFactory):
    def __new__(self):
        return FlyweightFactory.__new__(self, OwnerInfoFactory)
    
    def create(self, owner, quantity = 0):
        newInfo = OwnerInfo(owner, quantity)

        for info in self.flyweights:
            if info == newInfo:
                return info
        
        self._addFlyweight(newInfo)
        return newInfo

class OwnerInfo:
    def __init__(self, owner, quantity = 0):
        self._info = [owner, quantity]

    def getOwner(self):
        return self._info[0]

    def setOwner(self, owner):
        self._info[0] = owner

    def getQuantity(self):
        return self._info[1]

    def setQuantity(self, quantity):
        self._info[1] = quantity

    def __iter__(self):
        return self._info.__iter__()

    def __eq__(self, other):
        return self._info == other._info
        
