from dispenser import Dispenser
from purchase_handler import PurchaseHandler


welcome_message = """
    ===============================
    WELCOME TO OWONIKOKO STATTION
    ===============================
    PRESS 1 -> BUY PETROLUEM
    PRESS 2 -> SHOW TRANSACTION
    ===============================
    PRESS 3 -> TO EXIT
    ===============================
    """

available_products = """
            AVAILABLE PETROLEUM
            ========================
            1. PETROL   => 650/LITER
            2. DIESEL   => 720/LITER
            3. KEROSENE => 550/LITER
            4. GAS      => 480/LITER
            ========================
            0. EXIT
            =======================
            """

dispenser = Dispenser()
start = True
while start:
    user_choice = input(welcome_message)
    handler = PurchaseHandler(dispenser)
    if user_choice == "1":
        nozzle = True
        while nozzle:
            product_choice = input(available_products)
            if product_choice == "0": nozzle = False
            elif product_choice in ["1", "2", "3", "4"]: handler.handle_purchase(int(product_choice))
            else: print("Incorrect input\nPlease enter 1, 2, 3 or 4")
    elif user_choice == "2":
        transaction_log = len(dispenser.get_products())
        if transaction_log > 0:
            handler.get_purchase_history()
        else: print("No Transaction Available")
    elif user_choice == "3": start = False
    else: print("Incorrect input\nPlease enter 1, 2 or 3")


