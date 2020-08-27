# -*- coding : UTF-8 -*-

class ShoppingList:
    def __init__(self):
        self.clear()

    def clear(self):
        self.products = []
        self.realSum = 0

    def getProducts(self):
        return self.products

    def addProduct(self, product):
        self.products.append(product)

    def removeProduct(self, product):
        self.products.remove(product)

    def merge(self, other):
        self.products += other.products
        self.realSum += other.realSum

    def getTotalSum(self):
        return sum(product.price for product in self.products)

    def generateBill(self):
        bill = {}

        for product in self.products:
            bill = self.__addCosts(bill, product.costPerPerson())

        return bill

    def __addCosts(self, costs, other):
        for key in costs.keys():
            if key in other.keys():
                other[key] += costs[key]
            else:
                other[key] = costs[key]
        return other