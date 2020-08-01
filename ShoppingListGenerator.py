# -*- coding: UTF-8 -*-

from OCRConverter import OCRConverter
from BiedronkaTextParser import BiedronkaTextParser
from ShoppingList import ShoppingList
from Person import Person
from Product import Product

class ShoppingListGenerator:
    """Generates ShoppingList instance from given data
    
    * Sets product count to make 
    * even distribution between persons
    """

    def __init__(self, person_names):
        self.setPersons(person_names)

    def setPersons(self, person_names):
        self.persons = [Person(name) for name in person_names]

    def generateFromImage(self, image_file):
        converter = OCRConverter(image_file)
        data = converter.parseImageFile(image_file)
        return self.generateFromString(data)

    def generateFromString(self, string):
        parser = BiedronkaTextParser(string)
        products = parser.getProductList()
        return self.generateFromProducts(products, parser.getTotalSum())

    def generateFromProducts(self, products, realSum = 0):
        for (name, price) in products:
            product = Product(name, price)
            for person in self.persons:
                person.addProduct(product, 1/len(self.persons))

        shopping_list = ShoppingList()
        shopping_list.realSum = realSum
        for person in self.persons:
            shopping_list.addPerson(person)

        return shopping_list

    

        
        
        