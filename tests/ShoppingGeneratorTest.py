# -*- coding: UTF-8 -*-

import unittest
from ShoppingListGenerator import ShoppingListGenerator

NAMES = ["Andre", "Emma", "Iris"]
ITEMS = [("bread", 3.00), ("milk", 2.40), ("butter", 4.50)]

SHOPPING_LIST = """
        PARAGON FISKALNY
bread           1 x2,99   3,00C
milk            1 x2,85   2,40C
butter          1 x3,99   4.50A

SPRZEDAZ OPODATKOWANA A         4,50
SUMA PLN                        9,90
"""

class ShoppingGeneratorTest(unittest.TestCase):
    def testGenerateFromProducts(self):
        generator = ShoppingListGenerator(NAMES)
        shop_list = generator.generateFromProducts(ITEMS)

        products = shop_list.getProducts()
        name_price = set((product.name, product.price) for product in products)

        self.assertEqual(name_price, set(ITEMS))
        self.assertAlmostEqual(9.90, sum(shop_list.generateBill().values()))

        for person in shop_list.persons:
            self.assertAlmostEqual(person.getBill(), 3.30)

    def testGenerateFromString(self):
        generator = ShoppingListGenerator(NAMES)
        shop_list = generator.generateFromString(SHOPPING_LIST)

        products = shop_list.getProducts()
        name_price = set((product.name, product.price) for product in products)

        self.assertEqual(name_price, set(ITEMS))
        self.assertAlmostEqual(9.90, sum(shop_list.generateBill().values()))
        self.assertAlmostEqual(9.90, shop_list.realSum)

        for person in shop_list.persons:
            self.assertAlmostEqual(person.getBill(), 3.30)