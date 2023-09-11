# Date Script 

# Get user's name
user_name = input("Enter your name: ")

# Get the name of the person on the date with the user
date_name = input("Enter the name of the person you're on a date with: ")

# Get the user's budget for the date
budget = float(input("Enter your budget for the date: $"))

# Define a restaurant menu items
menu = {
    "appetizer": 10.0,
    "entree": 20.0,
    "dessert": 8.0,
    "cocktail": 12.0,
    "soda": 5.0
}

# Variables to keep track of the order cost
user_order_cost = 0.0

# Function to calculate remaining budget
def calculate_remaining_budget(total_budget, order_cost):
    return total_budget - order_cost

# Function to place an order
def place_order(person_name):
    global user_order_cost
    print(f"\n{person_name}'s turn to order:")
    for item, price in menu.items():
        while True:
            order_quantity = int(input(f"How many {item}s would {person_name} like to order? (0 to skip): "))
            if order_quantity < 0:
                print("Please enter a valid quantity.")
            else:
                break
        order_cost = order_quantity * price
        user_order_cost += order_cost
        print(f"{person_name} ordered {order_quantity} {item}(s) for a total of ${order_cost:.2f}")
        print(f"Remaining budget: ${calculate_remaining_budget(budget, user_order_cost):.2f}")

# Place orders for the user and the date
place_order(user_name)
place_order(date_name)

# Calculate the total bill
total_bill = user_order_cost

# Ask the user if they agree to pay the bill
agree_to_pay = input("\nDo you agree to pay the bill? (yes/no): ").lower()

# Check if they will get a second date based on their budget
if agree_to_pay == "yes" and total_bill <= budget:
    print(f"Remaining budget: ${calculate_remaining_budget(budget, total_bill):.2f}")
    print(f"\nCongratulations! {date_name} had a great time and agreed to a second date!.")
else:
    print(f"\nSorry, {user_name} the date did not go well. {date_name} left & you won't get a second date.")
