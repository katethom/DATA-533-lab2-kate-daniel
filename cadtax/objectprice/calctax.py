class calctax():
    def __init__(self, name, price, prov):
        objectprice.__init__(self, name, price, prov)

    def tax(self):

        if self.prov == 'bc':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.12 + self.price))
        if self.prov == 'alb':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
        if self.prov == 'sas':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.11 + self.price))
        if self.prov == 'man':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.13 + self.price))
        if self.prov == 'ont':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.13 + self.price))
        if self.prov == 'que':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.14975 + self.price))
        if self.prov == 'nb':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'pei':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'ns':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'nal':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.15 + self.price))
        if self.prov == 'yuk':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
        if self.prov == 'nwt':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
        if self.prov == 'nun':
            return print("the total price is for the item " + self.name + " is: " +"$" + str(self.price*0.05 + self.price))
