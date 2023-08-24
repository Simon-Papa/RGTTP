from collections import defaultdict

"""
  Lesson 4: ex3.py
"""

# 1. Create dictionary using comprehension
# {key, value = i, i**2}

print("Lesson 4, Ex 3.1\n"
      "Create comprehension dictionary\n")

comprehend: dict[int, int] = {i: i**2 for i in range(6)}

for key, value in comprehend.items():
    print("{:<2}".format(key), "{:>2}".format(value))

# 2. Create another comprehension and add +1 to each key's value.
# {key, value = i, i+1}

print("Lesson 4, Ex 3.2\n"
      "Create comprehension dictionary\n")

comprehend2: dict[int, int] = {i: i+1 for i in range(6)}

for key, value in comprehend2.items():
    print("{:<2}".format(key), "{:>2}".format(value))

# 3. Create 'fruits' defaultdict():
# apple: 10
# orange: 2
# banana: 3
# and for any other key set it's default value to 0

print("Lesson 4, Ex 3.3\n"
      "Create fruits defaultdict\n")

fruits: dict[str, int] = {"apple": 10, "orange": 2, "banana": 3}
fruits_default: defaultdict[str, int] = defaultdict(int)

fruits_default.update(fruits)
print(fruits_default["mandarin"])

# 4. Sort the 'fruits' dictionary using sorted() method
# by keys and values, dictionary does not have .sort()

print("Lesson 4, Ex 3.4\n"
      "Sort fruits by key & value\n")

print(sorted(fruits.keys()))
print(sorted(fruits.values()))

# 5. Return 'sorted_fruits' dictionary using sorted() method,
# sort by values.

print("Lesson 4, Ex 3.5\n"
      "Sort fruits dictionary by value\n")


def sort_value(item):
    return item[1]


fruits_sorted = dict(sorted(fruits.items(), key=sort_value))
print(type(fruits_sorted))
for key, value in fruits_sorted.items():
    print("{:<8}".format(key), "{:>2}".format(value))
print("\n")


# 6. Reverse the 'sorted_fruits' dictionary and print the dictionary.

print("Lesson 4, Ex 3.6\n"
      "Sort fruits dictionary in reverse by value\n")

fruits_reversed = dict(sorted(fruits.items(), key=sort_value, reverse=True))
for key, value in fruits_reversed.items():
    print("{:<8}".format(key), "{:>2}".format(value))
print("\n")
