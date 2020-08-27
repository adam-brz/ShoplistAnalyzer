# -*- coding: UTF-8 -*-

from OwnerGroup import OwnerGroupFactry
from OwnerInfo import OwnerInfoFactory

class Product:
    def __init__(self, name, price, ownerGroup = None):
        self.name = name
        self.price = price
        self.ownerGroup = ownerGroup

    def getOwners(self):
        owners = []

        if self.ownerGroup:
            owners = self.ownerGroup.getOwners()

        return owners

    def getQuantityForOwner(self, owner):
        if self.ownerGroup is None:
            return 0
        return self.ownerGroup.getQuantityForOwner(owner)

    def setQuantityForOwner(self, owner, quantity):
        groupFactory = OwnerGroupFactry()
        infoFactory = OwnerInfoFactory()

        newInfo = infoFactory.create(owner, quantity)
        self.ownerGroup = groupFactory.updateGroup(self.ownerGroup, newInfo)

    def costPerPerson(self):
        costs = {}

        if self.ownerGroup:
            for owner, quantity in self.ownerGroup:
                costs[owner] = quantity*self.price

        return costs
