# -*- coding: UTF-8 -*-

import unittest
from ShoppingList import ShoppingList
from OwnerGroup import OwnerGroupFactory
from OwnerInfo import OwnerInfoFactory
from Person import Person
from Product import Product

NAMES = ["Andre", "Emma", "Iris"]
ITEMS = [("bread", 3.00), ("milk", 2.40), ("butter", 4.50)]

class ShoppingListTest(unittest.TestCase):
    def testGetTotalSum(self):
        shopping_list = ShoppingList()

        for name, price in ITEMS:
            product = Product(name, price)            
            shopping_list.addProduct(product)

        self.assertEqual(shopping_list.getTotalSum(), 9.90)

    def testMerge(self):
        shopping_list1 = ShoppingList()
        shopping_list2 = ShoppingList()

        shopping_list1.addProduct(Product("Test", 2))
        shopping_list2.addProduct(Product("Test2", 4))

        shopping_list1.merge(shopping_list2)
        self.assertEqual(shopping_list1.getTotalSum(), 6)

    def testGenerateBill(self):
        shopping_list = ShoppingList()
        groupFactory = OwnerGroupFactory()
        infoFactory = OwnerInfoFactory()
        
        persons = []
        ownerInfoList = []

        for name in NAMES:
            person = Person(name)
            info = infoFactory.create(name, 0.33)

            ownerInfoList.append(info)
            persons.append(person)

        group = groupFactory.create(ownerInfoList)

        for name, price in ITEMS:
            product = Product(name, price, group)
            shopping_list.addProduct(product)

        expected = {}
        for name in NAMES:
            expected[name] = 9.90 * 0.33

        self.assertEqual(shopping_list.generateBill(), expected)


        

        