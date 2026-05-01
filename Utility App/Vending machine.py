# Vending Machine Program using Python - Assessment 2
# This program meets all core requirements and includes additional feature 
#to improve user experience and program structure.

import random  # Used for random suggestions - Module system


# ---------------- Nested Dictionary ---------------- #
# This dictionary stores all vending machine data:
# - Outer keys represent product categories 
# - Inner keys represent slot IDs
# - Values are dictionaries containing item details (name, price, stock)

vending_machine = {
    "Beverages": {
        "A1": {"name": "Apple Juice", "price": 3.00, "stock": 5},
        "A2": {"name": "Orange Juice", "price": 3.50, "stock": 5},
        "A3": {"name": "Sparkling Water", "price": 4.00, "stock": 5},
        "A4": {"name": "Masafi Water", "price": 3.00, "stock": 5},
        "A5": {"name": "Coca Cola", "price": 5.00, "stock": 5},
        "A6": {"name": "7 Up", "price": 5.00, "stock": 5},
        "A7": {"name": "Hot Coffee", "price": 5.00, "stock": 5}
    },
    "Savoury Snacks": {
        "B1": {"name": "Lays Chips", "price": 4.00, "stock": 5},
        "B2": {"name": "Doritos", "price": 4.00, "stock": 5},
        "B3": {"name": "Stix", "price": 3.00, "stock": 5},
        "B4": {"name": "Ritz Crackers", "price": 3.00, "stock": 5}
    },
    "Sweet Snacks": {
        "C1": {"name": "Snickers", "price": 3.95, "stock": 5},
        "C2": {"name": "Oreo", "price": 3.00, "stock": 5},
        "C3": {"name": "7-Days Croissant", "price": 3.00, "stock": 5},
        "C4": {"name": "Vanilla Cupcake", "price": 3.75, "stock": 5},
        "C5": {"name": "Galaxy", "price": 4.00, "stock": 5},
        "C6": {"name": "M&M Peanuts", "price": 3.50, "stock": 5}
    }
}

# Additional requirement - to suggest randomly after selection

# ---------------- Dictionary with List Values ---------------- #
# This dictionary stores suggestions based on item category:
# - Keys represent categories 
# - Values are lists of suggestion messages
# - Each list contains multiple suggestions for that category

suggestions = { 
    "Beverages": [
        "Suggestion: How about some Lays Chips (B1) for a salty snack?",
        "Suggestion: A Snickers bar (C1) would be a great sweet treat with this!",
        "Suggestion: A snack like chips or chocolate could go well with your drink.",
        "Suggestion: Need a crunch? Try the Ritz Crackers (B4)."
    ],
    "Savoury Snacks": [
        "Suggestion: Wash those chips down with a cold Coca Cola (A5)!",
        "Suggestion: Stay hydrated with a Masafi Water (A4).",
        "Suggestion: A drink might go well with this snack.",
        "Suggestion: A Sparkling Water (A3) goes great with savory snacks."
    ],
    "Sweet Snacks": [
        "Suggestion: A hot coffee or Orange Juice (A2) pairs well with sweets!",
        "Suggestion: A cold drink might go well with this snack.",
        "Suggestion: Balance the sugar with some Sparkling Water (A3).",
    ] 
}

# ---------------- Functions ---------------- #
#Additional requirement : Use of functions to improve structure
#Core requirement: Presenting a menu via the console

def display_menu(): # This function displays the vending machine menu in a structured format.

    print("\n------ VENDING MACHINE MENU ------")

    # Loop through each category in menu
    for category in vending_machine:
        print(f"\n--- {category.upper()} ---")

       # Get items in this category
        items = vending_machine[category]

        # Loop through each slot
        for slot in items:
            item = items[slot]

            # Extract details
            name = item['name']
            price = item['price']
            stock = item['stock']

            # Print formatted output
            print(f"{slot}: {name:<25} | AED {price:<5} | Stock: {stock}")

        print()  # blank line between categories
    print("\n==================================")

# Core requirement: A way of capturing the user’s inputted code
# This function searches for an item based on the slot ID entered by the user.

def find_item(slot_code): 
    for category, items in vending_machine.items():  # Loop through categories and items
        if slot_code in items:      # checks if slot-ID exists
            return category, items[slot_code]
    return None, None   # returns None if not found


#Additional requirement: quantity validation + stock handling
# This function validates the quantity entered by the user.
def get_quantity(stock_amount):
    while True:
        # Error handling
        try:
            quantity = int(input("Enter quantity: "))   # takes user input
            if quantity <= 0:
                print("Please enter a quantity greater than 0.")
            elif quantity > stock_amount:
                print(f"Only {stock_amount} available. Enter quantity again.")   # limits quantity to stock
            else:
                return quantity
            # Prevents program crash
        except ValueError:
            print("Please enter a whole number.") # handles non-numeric input

# Core Requirement: A way of managing money. User inputs any amount.
# This function manages the payment process for the transaction.
def take_money(total_cost):
    money = 0.0 # tracks the inserted amount
    while money < total_cost:   # loop until paid
        print(f"Amount inserted so far: AED {money:.2f}")
        user_input = input("Insert money or type cancel: ").strip().lower()
        if user_input == "cancel": # cancels transaction
            return None
        try:
            amount = float(user_input) # convert input
            if amount <= 0:     # invalid amount
                print("Please enter an amount greater than 0.")
                continue
            money += amount
            if money < total_cost:
                remaining = total_cost - money
                print(f"Insufficient funds. You still need: AED {remaining:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number or type cancel.")
    return money # return total paid

#  Core Requirement: providing a final bill reciept
# This function generates and displays the final receipt after a purchase.
def print_receipt(item_name, price, quantity, total_paid, change):
    total_cost = price * quantity # calculates total cost
       
    print("\n========= RECEIPT =========") # prints final receipt
    print(f"{item_name} x {quantity} - AED{total_cost:.2f}")
    print("--------------------------")
    print(f"TOTAL PAID: AED{total_paid:.2f}")
    print(f"CHANGE: AED{change:.2f}")
    print("==========================")

# ---------------- Main Program - Vending Machine Logic control ---------------- #

# This function controls the overall vending machine program.
def main():
    print("\n WELCOME - PLEASE MAKE SELECTION") #standard display opening message 
    while True:
        display_menu()

# Core Requirement: A way of capturing the user’s inputted code
        user_code = input("\nEnter slot ID: ").strip().upper()
        category, selected_item = find_item(user_code)

        if selected_item is None:
            print("Invalid slot ID. Please try again.")
            input("Press Enter to continue...")
            continue
        # restarts loop if invalid

# Additional Requirement: A stock system (Running out of products)
        if selected_item["stock"] <= 0:
         print("\n Sorry, this item is out of stock.")# to prevent purchase if no stock
         input("Press Enter to return to menu...")  # back to menu 
         continue
        else:
            print(f"\nYou selected: {selected_item['name']}")
            print(f"Price per item: AED {selected_item['price']:.2f}")

# random.choice picks one suggestion from the list above 
            print(random.choice(suggestions[category]))
            quantity = get_quantity(selected_item["stock"])
            total_cost = selected_item["price"] * quantity
            print(f"Total cost: AED{total_cost:.2f}")

# Core Requirement: Money management and correct change returned
            money = take_money(total_cost)
            if money is None:
                print("Transaction cancelled. Change returned.")
                continue
            change = money - total_cost     # calculates change
            selected_item["stock"] -= quantity      # Updating stock system

#  Core Requirement: Dispensing message for the user
            print(f"\nDispensing: {selected_item['name']} x {quantity}")
            print("Items added to tray.")

# Core Requirement: A message that tells the user how much change received
            print(f"Change returned: AED {change:.2f}")
            print_receipt(
                selected_item["name"],
                selected_item["price"],
                quantity,
                money,
                change
            )
# Additional Requirement: A way of allowing users to buy additional items
        while True:
            again = input("\nDo you want to buy another item? (yes/no): ").strip().lower()
            if again == "yes":
                break  # go back to main loop
            elif again == "no":
                print("THANK YOU! HAVE A NICE DAY.") # Upon completion , a ending message.
                return  # exit program
            else:
                print("Invalid input. Please enter YES or NO.")


# Runs program - using main function call 
if __name__ == "__main__":
    main()
