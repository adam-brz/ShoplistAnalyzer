import unittest
from OwnerGroup import OwnerGroupFactory
from OwnerInfo import OwnerInfoFactory
from Product import Product

class ProductTest(unittest.TestCase):
    def testCreateProduct(self):
        product = Product("Test", 10)

        self.assertEqual(product.name, "Test")
        self.assertEqual(product.price, 10)
        self.assertEqual(product.costPerPerson(), {})

    def testGetCostsPerPerson(self):
        groupFactory = OwnerGroupFactory()
        infoFactory = OwnerInfoFactory()

        info1 = infoFactory.create("Me", 0.25)
        info2 = infoFactory.create("You", 0.75)

        group = groupFactory.create([info1, info2])
        product = Product("Test", 12, group)

        self.assertEqual(product.costPerPerson(), {"Me": 3, "You": 9})