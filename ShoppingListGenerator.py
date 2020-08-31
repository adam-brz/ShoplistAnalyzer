# -*- coding: UTF-8 -*-

from ShoppingList import ShoppingList
from OwnerGroup import OwnerGroupFactory
from OwnerInfo import OwnerInfoFactory
from Person import Person
from Product import Product

from ocr.OCRConverter import OCRConverter
from ocr.BiedronkaTextParser import BiedronkaTextParser

class ShoppingListGenerator:
    def __init__(self, person_names):
        self.setPersons(person_names)

    def setPersons(self, person_names):
        self.persons = [Person(name) for name in person_names]

    def generateFromImage(self, image_file):
        converter = OCRConverter()
        data = converter.parseImageFile(image_file)
        return self.generateFromString(data)

    def generateFromString(self, string):
        parser = BiedronkaTextParser(string)
        products = parser.getProductList()
        return self.generateFromProducts(products, parser.getTotalSum())

    def generateFromProducts(self, products, realSum = 0):
        shopping_list = ShoppingList()
        shopping_list.realSum = realSum

        groupFactory = OwnerGroupFactory()
        infoFactory = OwnerInfoFactory()

        infoList = [infoFactory.create(person, 1/len(self.persons)) 
                        for person in self.persons]

        defaultGroup = groupFactory.create(infoList)

        for (name, price) in products:
            product = Product(name, price, defaultGroup)
            shopping_list.addProduct(product)
        
        return shopping_list

    

        
        
        