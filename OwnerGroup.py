# -*- coding : UTF-8 -*-

from FlyweightFactory import FlyweightFactory

class OwnerGroupFactry(FlyweightFactory):
    def __new__(self):
        return FlyweightFactory.__new__(self, OwnerGroupFactry)

    def updateGroup(self, group, newInfo):
        oldInfo = list(group) if group else []

        for info in oldInfo:
            if info.getOwner() == newInfo.getOwner():
                oldInfo.remove(info)
                break

        oldInfo.append(newInfo)
        return self.create(oldInfo)

    def create(self, ownerInfoList):
        for ownerGroup in self.flyweights:
            matched = 0

            for ownerInfo in ownerInfoList:
                if ownerInfo in ownerGroup:
                    matched += 1

            if matched == len(ownerGroup) == len(ownerInfoList):
                return ownerGroup

        newGroup = OwnerGroup(ownerInfoList)
        self._addFlyweight(newGroup)

        return newGroup

class OwnerGroup(tuple):
    def __new__(self, ownerInfoList):
        return tuple.__new__(OwnerGroup, ownerInfoList)

    def getOwners(self):
        return [ownerInfo.getOwner() for ownerInfo in self]

    def getQuantityForOwner(self, owner):
        for ownerInfo in self:
            if owner == ownerInfo.getOwner():
                return ownerInfo.getQuantity()

        return 0



