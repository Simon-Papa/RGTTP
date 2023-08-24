"""
  Lesson 4: ex1.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2

print("Lesson 4, Ex 1.1\n"
      "Fruits dictionary created\n")

fruits: dict[str, int] = {"apple": 10, "orange": 2}

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")


# 2. Add banana to the dictionary and set it's value to 3

print("Lesson 4, Ex 1.2\n"
      "Add 'banana' to fruits dictionary\n")

fruits["banana"] = 3

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")

# 3. Add mandarin using dictionary method .update()

print("Lesson 4, Ex 1.3\n"
      "Add 'mandarin' to fruits dictionary using the 'update' method\n")

fruits.update({"mandarin": 0})

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")


# 4. Remove the mandarin from the dictionary

print("Lesson 4, Ex 1.4\n"
      "Remove 'mandarin' from fruits dictionary\n")

fruits.popitem()

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")


# 5. Add 10 more apples and remove 2 bananas

print("Lesson 4, Ex 1.5\n"
      "Add 10 aaples and remove 2 bananas\n")

fruits["apple"] += 10
fruits["banana"] -= 2

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")


# 6. Remove 'apple' from the dictionary using .pop()
#    and save it's value into a variable 'apples'

print("Lesson 4, Ex 1.6\n"
      "Remove 'apple' using .pop method and save its value in a variable\n"
      "'apples'\n")

apples: int = fruits.pop("apple")

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print()
print("Apples =", apples)
print("\n")


# 7. Remove 'mandarin' from the dictionary using .pop()
#    and save it's value into a variable 'mandarin'
#    if 'mandarin' doesn't exist set the variable to 0

print("Lesson 4, Ex 1.7\n"
      "Remove 'mandarin' using .pop method and save its value in a variable\n"
      "'mandarins'. If 'mandarin' doesn't exist, set the variable to '0'\n")

try:
    fruits.pop("mandarin")
except KeyError:
    mandarins = 0

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print()
print("Mandarins =", mandarins)
print("\n")


# 8. Remove last item from the dictionary using .popitem()
#    and save it's value into variable 'last'

print("Lesson 4, Ex 1.8\n"
      "Remove the last item using the .popitem method and save its value in\n"
      "a variable 'last'\n")

last: tuple = fruits.popitem()

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print()
print("Last =", last[1])
print("\n")

# 9. Check if the 'banana' is in the fruits dictionary.

print("Lesson 4, Ex 1.9\n"
      "Check if 'banana' is in the 'fruits' dictionary\n")

if fruits.get("banana") is None:
    print("'banana' is not in the Dictionary")

    # Alternate Method:

if "banana" not in fruits:
    print("'banana' is not in the Dictionary")
