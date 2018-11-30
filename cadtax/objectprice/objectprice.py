class objectprice():
    def __init__(self, name, price, prov):
        self.name = name
        self.price = price
        self.prov = prov

    def getprice(self):
        return calctax.tax(self)
