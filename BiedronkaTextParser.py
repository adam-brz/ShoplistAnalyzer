# -*- coding : UTF-8 -*-

from OCRConverter import OCRConverter
import re

class ParseException(Exception): pass

class BiedronkaTextParser(object):
    def __init__(self, text_block):
        self.data = text_block
        
    def getProductList(self):
        products = []
        
        raw_products = self.__getRawProductText()
        discount_text_blocks = self.__getDiscountTextBlocks(raw_products)
        raw_products = self.__removeDiscountFromProductText(raw_products, discount_text_blocks)

        products += self.__getAllDiscounts(discount_text_blocks)
        raw_products = [line for line in raw_products.splitlines() if line]
        
        for product in raw_products:
                products.append(self.__parseProduct(product))
            
        return products
        
    def getTotalSum(self):
        result = re.search(r"PLN +\d+, ?\d\d", self.data)

        if result is None:
            return 0

        totalSum = self.data[result.start() + len("PLN ") : result.end()]
        totalSum = totalSum.replace(",", ".").strip()
        
        return float(totalSum)
        
    def __getRawProductText(self):
        REGEX_START = "FISKALNY"
        REGEX_END = "SPRZEDA(Z|Ż|z|ż) (OPODATKO(W|K)ANA|OPODATK.)"

        start = re.search(REGEX_START, self.data)
        end = re.search(REGEX_END, self.data)
        
        if not end or not start:
            return ""

        return self.data[start.end() : end.start()]

    def __getDiscountTextBlocks(self, raw_products):
        discountPattern = "\n.*\nRabat -\\d+,\\d\\d\n\\d+,\\d\\d"
        return re.findall(discountPattern, raw_products)

    def __removeDiscountFromProductText(self, productText, rawDiscounts):
        for discount in rawDiscounts:
            productText = productText.replace(discount, "")
        return productText

    def __getAllDiscounts(self, discount_text_blocks):
        parsedDiscounts = []
        for discount in discount_text_blocks:
            parsedDiscounts.append([el for el in discount.splitlines() if el])

        discountedProducts = []
        for parsed in parsedDiscounts:
            product = self.__parseProduct(parsed[0])
            newPrice = float(parsed[2].replace(",", "."))
            discountedProducts.append((product[0], newPrice))

        return discountedProducts

    def __parseProduct(self, productText):
        productNamePattern = r"^\D+"
        pricePattern = r"\d+(,|.)\d\d(A|B|C|4|0)$"

        productName = re.search(productNamePattern, productText)
        productPrice = re.search(pricePattern, productText)

        if productName is None:
            return ("INVALID", 0)
        
        productName = productText[productName.start() : productName.end()].strip()

        if productPrice is None:
            return (productName, 0)

        productPrice = productText[productPrice.start() : productPrice.end() - 1]
        productPrice = productPrice.replace(",", ".")

        return (productName, float(productPrice))
