# -*- coding: UTF-8 -*-

import unittest
from ShoppingList import ShoppingList
from Person import Person
from Product import Product

NAMES = ["Andre", "Emma", "Iris"]
ITEMS = [("bread", 3.00), ("milk", 2.40), ("butter", 4.50)]

class ShoppingListTest(unittest.TestCase):
    def testAddPerson(self):
        shopping_list = ShoppingList()

        for name in NAMES:
            person = Person(name)            
            shopping_list.addPerson(person)

            self.assertTrue(person in shopping_list.persons)

    def testRemovePerson(self):
        shopping_list = ShoppingList()
        persons = [Person(name) for name in NAMES]

        for person in persons:        
            shopping_list.addPerson(person)

        for person in persons:        
            shopping_list.removePerson(person)
            self.assertFalse(person in shopping_list.persons)

    def testGetProducts(self):
        shopping_list = ShoppingList()

        i = 0
        for name in NAMES:
            person = Person(name)
            product = Product(ITEMS[i][0], ITEMS[i][1])
            person.addProduct(product)
            
            shopping_list.addPerson(person)
            i += 1

        products = set(item.name for item in shopping_list.getProducts())
        expected = set(item[0] for item in ITEMS)

        self.assertEqual(products, expected)

    def testGenerateBill(self):
        shopping_list = ShoppingList()
        persons = [Person(name) for name in NAMES]
        products = [Product(x[0], x[1]) for x in ITEMS]

        for person in persons:
            shopping_list.addPerson(person)

        for i in range(len(persons)):
            persons[i].addProduct(products[i])

        expected = {}
        for i in range(len(NAMES)):
            expected[NAMES[i]] = ITEMS[i][1]

        self.assertEqual(shopping_list.generateBill(), expected)


        

        