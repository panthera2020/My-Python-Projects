from card_validation import CardValidation

credit_card = CardValidation()

print("Hello, kindly enter card details to verify")
try:
    card_number = int(input())
except ValueError:
    print()
    print("ENTER VALID CARD NUMBER!!!")
    exit(0)

print()
print("**********************************************")
print("**Credit card type: ", credit_card.card_type(card_number))
print("**Credit card number: ", card_number)
print("**Credit card length: ", credit_card.get_length(card_number))
print("**Credit card validity: ", ("Valid" if credit_card.is_card_valid(card_number) else "Invalid"))
print("**********************************************")