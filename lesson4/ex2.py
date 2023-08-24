"""
  Lesson 4: ex2.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2
# banana: 3

print("Lesson 4, Ex 2.1\n"
      "Fruits dictionary created\n")

fruits: dict[str, int] = {"apple": 10,
                          "orange": 2,
                          "banana": 3}


# 2. Iterate over fruits in fruits dictionary using for loop,
#    print using f-strings:
#    apple: 10
#    orange: 2
#    banana: 3

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")

# 2. Iterate over the keys in 'fruits' dictionary

print("Lesson 4, Ex 2.2\n"
      "Iterate over the fruits in the dictionary using a 'for' loop, print\n"
      "using f-strings\n")

for key in fruits.keys():
    print(f"{key}")
print("\n")


# 3. Iterate over the values in dictionary

print("Lesson 4, Ex 2.3\n"
      "Iterate over the values in the dictionary using a 'for' loop, print\n"
      "using f-strings\n")

for value in fruits.values():
    print(f"{value}")
print("\n")


# 4. Access value banana using .get() method

print("Lesson 4, Ex 2.4\n"
      "Access the value of 'banana' using .get\n")

print(fruits.get("banana"))
print("\n")

# 5. Access value mandarin using .get() method,
#    if 'mandarin' doesn't exist, return 0

print("Lesson 4, Ex 2.5\n"
      "Access the value of 'mandarin' using .get. If 'mandarin isn't in the\n"
      "list, return 0\n")

print(fruits.get("mandrin", 0))
print("\n")


# 6. Remove all items from the dictionary

print("Lesson 4, Ex 2.6\n"
      "Remove all items from the Dictionary\n")

fruits.clear()

for keys, values in fruits.items():
    print("{:<8}".format(keys), ":", "{:>3}".format(values))
print("\n")
