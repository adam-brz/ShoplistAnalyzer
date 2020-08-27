import unittest
from OwnerInfo import OwnerInfo, OwnerInfoFactory

class OwnerInfoTest(unittest.TestCase):
    def testFactorySingleton(self):
        instance = OwnerInfoFactory()
        instance2 = OwnerInfoFactory()

        self.assertIs(instance, instance2)

    def testFactoryCreate(self):
        factory = OwnerInfoFactory()
        info = factory.create("Test", 1)

        self.assertEqual(info.getOwner(), "Test")
        self.assertEqual(info.getQuantity(), 1)

    def testFactoryCreateOneInstance(self):
        factory = OwnerInfoFactory()

        info = factory.create("Unique", 1)
        info2 = factory.create("Unique", 1)
        self.assertIs(info, info2)

    def testFactoryCreateManyInstances(self):
        factory = OwnerInfoFactory()

        info = factory.create("Unique", 0.5)
        info2 = factory.create("Unique", 1)
        info3 = factory.create("Not Unique", 1)
        
        self.assertIsNot(info, info2)
        self.assertIsNot(info, info3)
        self.assertIsNot(info2, info3)
