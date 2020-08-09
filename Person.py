# -*- coding : UTF-8 -*-

class Person:
    def __init__(self, name):
        self.name = name
        self.bought_products = {}

    def addProduct(self, product, count = 1):
        self.bought_products[product] = count

    def setProductCount(self, product, count = 1):
        self.bought_products[product] = count

    def getProductCount(self, product):
        return self.bought_products[product]

    def removeProduct(self, product):
        if product in self.bought_products:
            self.bought_products.pop(product)

    def getProducts(self):
        return set(self.bought_products.keys())

    def getBill(self):
        return sum(product.price*count for product, count in self.bought_products.items())
