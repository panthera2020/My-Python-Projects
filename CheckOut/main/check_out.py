from item import item

class CheckOut:
    def __init__(self):
        self.items = []

    def get_item(self): return self.items

    def addItem(self, product, quantity, price):
        self.new_item = item()
        self.new_item.setName(product)
        self.new_item.setQuantity(quantity)
        self.new_item.setPrice(price)
        self.items.append(self.new_item)

    def get_subtotal(self):
        sum = 0.0
        for item in self.items: sum += item.getTotalPrice()
        return sum

    def get_discount(self, discount): return (discount / 100) * self.get_subtotal()

    def get_vat(self): return (7.5 / 100) * self.get_subtotal()

    def get_total_bill(self, discount): return self.get_subtotal() - self.get_discount(discount) + self.get_vat()

    def get_change(self, amount, discount): return amount - (self.get_total_bill(discount))

