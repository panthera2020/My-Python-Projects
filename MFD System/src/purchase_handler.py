from Product import Product

class PurchaseHandler:

    def __init__(self, dispenser):
        self.dispenser = dispenser

    def handle_purchase(self, product_choice):
        new_products = Product()
        new_products.set_product_type(product_choice)
        product_name = new_products.get_product_name()
        product_value = int(new_products.ProductType.value)

        while True:
            liters_or_amount = input("Enter liters or amount: ").lower()
            if liters_or_amount in ["liters", "amount"]:
                break
            print("Incorrect input\nPlease enter liters or amount")

        if liters_or_amount == "amount":
            while True:
                amount = float(input(f"How much {product_name} are you buying ({product_value}/L): "))
                if amount < product_value:
                    print("Amount must be above a liter price!!!")
                else:
                    new_products.set_liter_of(amount)
                    break

        elif liters_or_amount == "liters":
            while True:
                liters = float(input(f"How many liters of {product_name} are you buying ({product_value}/L): "))
                if liters <= 0: print("Liters must be above zero!!!")
                else:
                    new_products.set_amount_of(liters)
                    break

        self.dispenser.add_product(new_products)
        receipt = self.dispenser.get_last_product()

        print("Customer Transaction Receipt")
        print("=======================================")
        print(f"=   Product:    {receipt.get_product_name()}   =")
        print(f"=   Amount:     {receipt.get_amount()}         =")
        print(f"=   Liters:     {receipt.get_liter()}          =")
        print("=   Thank you for your Patronage                =")
        print("=======================================")
        print("Saving Transaction History.......")