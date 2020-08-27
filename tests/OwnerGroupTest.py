import unittest
from OwnerGroup import OwnerGroup, OwnerGroupFactry
from OwnerInfo import OwnerInfoFactory

class OwnerGroupTest(unittest.TestCase):
    def testFactorySingleton(self):
        instance = OwnerGroupFactry()
        instance2 = OwnerGroupFactry()

        self.assertIs(instance, instance2)

    def testGroupCreate(self):
        groupFactory = OwnerGroupFactry()
        infoFactory = OwnerInfoFactory()

        info1 = infoFactory.create("Me", 1)
        info2 = infoFactory.create("You", 2)

        group = groupFactory.create([info1, info2])

        self.assertIsNotNone(group)
        self.assertEqual(len(group), 2)

    def testGroupCreateOnce(self):
        groupFactory = OwnerGroupFactry()
        infoFactory = OwnerInfoFactory()

        info1 = infoFactory.create("Me", 1)
        info2 = infoFactory.create("You", 2)

        group1 = groupFactory.create([info1, info2])
        group2 = groupFactory.create([info1, info2])
        group3 = groupFactory.create([info2, info1])

        self.assertIs(group1, group2)
        self.assertIs(group1, group3)

    def testGroupCreateMany(self):
        groupFactory = OwnerGroupFactry()
        infoFactory = OwnerInfoFactory()

        info1 = infoFactory.create("Me", 1)
        info2 = infoFactory.create("You", 2)
        info3 = infoFactory.create("Him", 1)

        group1 = groupFactory.create([info1, info2])
        group2 = groupFactory.create([info1, info2, info3])

        self.assertIsNot(group1, group2)
    