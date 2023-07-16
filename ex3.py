"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

print("Mum's Pasta" * 42)

# 2. Insert space between each output and print it out again.

print(("Mum's Pasta" + " ") * 41 + "Mum's Pasta")

# 3. Save your favourite food into a variable and print it out 42 times

favourite_food: str = "Mum's Pasta"
print(favourite_food*42)

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

rc_favourite_food: str = "sushi"
favourite_food, rc_favourite_food = rc_favourite_food, favourite_food
print(favourite_food, " ", rc_favourite_food)
