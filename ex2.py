"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.

list_shopping: list = ["Apples", "Milk", "Bread", "Chicken", "Pasta"]
print(list_shopping)

# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.

list_shopping_total_cost: float = 2.99 + 1.79 + 3.49 + 6.99 + 2.49
print(list_shopping_total_cost)

# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?

list_shopping_total_cost = 2.99 + (1.79*5) + 3.49 + 6.99 + 2.49
print(list_shopping_total_cost)

# 4. Print out every item of your shopping list on a new line.

for x in list_shopping:
    print(x)
