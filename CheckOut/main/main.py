from datetime import datetime

from check_out import CheckOut

cashier = CheckOut()

customer_name = input("What is the customer name? ")

user_choice = ""

while user_choice != "no":
    item_name = input("What did the user buy? ")
    quantity = int(input("How many pieces? "))
    price = float(input("How much per unit? "))
    cashier.addItem(item_name, quantity, price)
    user_choice = input('Add more item? (yes/no) )')

print()
discount = float(input('How much discount will the user get? '))
cashier_name = input("What is the cashier name? ")
print()

store_message = """
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL NO: 03293828343 """

print(store_message)
print("Date: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Cashier: ",cashier_name)
print("Custer Name: ",customer_name)
print("===========================================================================")
print(f'{"ITEMS": <15}{"QUANTITY": >5}{"PRICE": >10}{"TOTAL(NGN)": >10}')
print("===========================================================================")
items = cashier.get_item()
for item in items:
    print(f'{item.getName(): <15} {item.getQuantity(): >5} {item.getPrice(): >10} {item.getTotalPrice(): >10}')
print()
print("---------------------------------------------------------------------------")
print(f'{"Sub Total": <25} {cashier.get_subtotal()}')
print(f'{"Discount": <25} {cashier.get_discount(discount)}')
print(f'{"Vat @ 7.5%" : <25} {cashier.get_vat()}')
print("===========================================================================")
print(f'{"Bill Total": <25}{cashier.get_total_bill(discount)}')
print("===========================================================================")
print("THIS IS NOT A RECEIPT, KINDLY PAY ", cashier.get_total_bill(discount))
print("===========================================================================")

print()
amount_given = int(input("How much did the user give? "))

print()
print(store_message)
print("Date: ",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Cashier: ",cashier_name)
print("Custer Name: ",customer_name)
print("===========================================================================")
print(f'{"ITEMS": <15}{"QUANTITY": >5}{"PRICE": >10} {"TOTAL(NGN)": >10}')
print("===========================================================================")
items = cashier.get_item()
for item in items:
    print(f'{item.getName(): <15} {item.getQuantity(): >5} {item.getPrice(): >10} {item.getTotalPrice(): >10}')
print()
print("---------------------------------------------------------------------------")
print(f'{"Sub Total": <25} {cashier.get_subtotal(): <5}')
print(f'{"Discount": <25} {cashier.get_discount(discount): <5}')
print(f'{"Vat @ 7.5%" : <25} {cashier.get_vat(): <5}')
print("===========================================================================")
print(f'{"Bill Total: ": <25}{cashier.get_total_bill(discount) : <5}')
print(f'{"Amount: " : <25}{amount_given : <5}')
print(f'{"Balance: " : <25}{cashier.get_change(amount_given, discount) : <5}')
print("===========================================================================")
print("      THANKS FOR YOUR PATRONAGE         ")
print("===========================================================================")




