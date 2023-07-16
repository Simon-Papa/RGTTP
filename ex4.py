"""
  Lesson 1: ex4.py
"""

# 1. Create a new list with the following values:
#    Apple, Milk, Bread, Chicken and Pasta

list_food: list = ["Apple", "Milk", "Bread", "Chicken", "Pasta"]

# 2. Write a check to see if Orange is in the shopping list or not.

if "Orange" in list_food:
    print("Orange made the list.")
else:
    print("Orange didn't make the cut.")

# 3. Write a function "in_shopping_list" that takes a item such as
#    orange, and returns True or False.
#    Depending whether the item is in the list or not.


def in_shopping_list(food: str) -> bool:
    if food in list_food:
        return True
    else:
        return False

# 4. Write a function "show_shopping_list" that will return a
#    shopping list and print it out on the screen.


def show_shopping_list() -> list:
    return list_food


for x in list_food:
    print(x)


# 5. Create a list of the following values: 2.99 1.79 3.49 6.99 2.49

list_prices: list = [2.99, 1.79, 3.49, 6.99, 2.49]

# 6. Create a function price_checker, and pass this list as
#    an argument and let the function return the cheapest price.#


def price_checker(y: list) -> float:
    return min(y)

# 7. Write another function show_price, that will call your
#    price_checker function and uses the result to
#    print the cheapest price.


def show_price():
    lowest_price = price_checker(list_prices)
    print(lowest_price)


show_price()
