class item:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.quantity = 0

    def setName(self,name): self.name = name

    def setPrice(self,price): self.price = price

    def setQuantity(self,quantity): self.quantity = quantity

    def getName(self): return self.name

    def getPrice(self): return self.price

    def getQuantity(self): return self.quantity

    def getTotalPrice(self): return self.price * self.quantity



