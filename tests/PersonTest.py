# -*- coding: UTF-8 -*-

import unittest

from Person import Person
from Product import Product

class PersonTest(unittest.TestCase):
    def testAddProduct(self):
        person = Person("Some Name")
        product = Product("Product", 2.50)

        person.addProduct(product, 2)

        self.assertEqual(len(person.getProducts()), 1)
        self.assertEqual(person.getProducts().pop(), product)

    def testRemoveProduct(self):
        person = Person("Some Name")
        product = Product("Product", 2.50)

        person.addProduct(product)
        person.removeProduct(product)

        self.assertEqual(len(person.getProducts()), 0)

    def testGetBillSingle(self):
        person = Person("Some Name")
        product = Product("Product", 2.50)

        person.addProduct(product, 0.8)
        self.assertAlmostEqual(person.getBill(), 2.0)

    def testGetBillMultiple(self):
        person = Person("Some Name")
        product = Product("Product", 2.50)
        product2 = Product("Product2", 1)

        person.addProduct(product, 1)
        person.addProduct(product2, 2)

        self.assertAlmostEqual(person.getBill(), 4.50)