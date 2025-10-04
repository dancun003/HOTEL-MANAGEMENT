import secrets
import string
import random

def generate_reservation_code():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    
    while True:
        r_code = ''.join(secrets.choice(alphabet) for _ in range(5))
        
        if (any(c.islower() for c in r_code)
            and any(c.isupper() for c in r_code)
            and any(c.isdigit() for c in r_code)
            and any(c in "!@#$%^&*()-_=+" for c in r_code)):
            return r_code  


def assign_table(name, r_code):
    tables = list(range(1, 101))
    assigned_table = random.choice(tables)

    print(f"\nHello {name}, welcome to Six Star Hotel!")
    print(f"Your secure reservation code is: {r_code}")
    print(f"Your assigned table number is: {assigned_table}")
    print("Please present your code at the reception to confirm your reservation.\n")


def food_ordering():
    """Displays the hotel menu and allows multiple orders with quantity and item number support."""
    menu = {
        "ugali-kuku": 100,
        "ugali-nyama": 150,
        "ugali-mayai": 90,
        "steamed rice": 120,
        "juice": 100,
        "nyama choma": 300,
        "kebabs": 230,
        "pizza": 1200,
        "steamed fish": 900,
        "crabs": 600,
        "coffee": 150
    }

    menu_items = list(menu.items())

    print("--- Six Star Hotel Menu ---")
    for index, (item, price) in enumerate(menu_items, start=1):
        print(f"{index}. {item.title():<20} - Ksh {price}")
    
    order_list = []
    total = 0

    while True:
        order = input("\nEnter item name or number (or type 'done' to finish): ").strip().lower()

        if order == "done":
            break

        if order.isdigit():
            order_index = int(order) - 1
            if 0 <= order_index < len(menu_items):
                item, price = menu_items[order_index]
            else:
                print("Invalid number. Please select a valid menu item.")
                continue
        elif order in menu:
            item, price = order, menu[order]
        else:
            print("Item not found. Please try again.")
            continue

        try:
            qty = int(input(f"Enter quantity for {item.title()}: "))
            if qty <= 0:
                print("Quantity must be at least 1.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        order_list.append((item, qty, price * qty))
        total += price * qty
        print(f"Added {qty} x {item.title()} (Ksh {price * qty})")

    if order_list:
        print("\n--- Order Summary ---")
        for item, qty, cost in order_list:
            print(f"- {item.title():<20} x{qty:<2}  Ksh {cost}")
        print(f"\nTotal bill: Ksh {total}")
    else:
        print("\nYou did not order anything.")
    
    print("\nThank you for dining with Six Star Hotel!")
    return total  


def payment(total):
    attempts = 4
    
    while attempts > 0:
        try:
            pay = int(input(f"\nYour total is Ksh {total}. Enter amount to pay: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            attempts -= 1
            continue

        if pay < total:
            print(f"Insufficient payment. You still owe Ksh {total - pay}. Try again.")
            attempts -= 1
        elif pay > total:
            print(f"Payment accepted. Your change is Ksh {pay - total}.")
            break
        else:
            print("Payment successful. Thank you!")
            break

        if attempts == 0:
            print("\nYou have exceeded the maximum number of attempts.")
            print("Please visit the reception for assistance.")
    
name = input("Enter your name: ").strip()

if len(name) > 0:
    r_code = generate_reservation_code()
    assign_table(name, r_code)
    total = food_ordering()   
    if total > 0:
        payment(total)    
else:
    print("Please enter a valid name to proceed.")
