# -*- coding : UTF-8 -*-

class ShoppingList:
    def __init__(self):
        self.persons = []
        self.bill = {}
        self.realSum = 0

    def getProducts(self):
        products = set()

        for person in self.persons:
            products = products.union(person.getProducts())

        return products
    
    def addPerson(self, person):
        self.persons.append(person)

    def removePerson(self, person):
        self.persons.remove(person)

    def getTotalSum(self):
        return sum(person.getBill() for person in self.persons)

    def generateBill(self):
        self.bill = {}

        for person in self.persons:
            self.bill[person.name] = round(person.getBill(), 2)

        return self.bill