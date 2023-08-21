"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:

shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

shopping_list_sorted: list = sorted(shopping_list)
print("Lesson 3, Ex3.1\n",
      shopping_list_sorted)

# 2. Sort the list using .sort() method and print that list

shopping_list.sort()
print("Lesson 3, Ex3.2\n",
      shopping_list)

# 3. Use the built-in function reversed(), reverse the list and print that list

shopping_list_reverse: list = list(reversed(shopping_list))
print("Lesson 3, Ex3.3\n",
      shopping_list_reverse)


# 4. Reverse the list using sort() method and print the list

shopping_list.sort(reverse=True)
print("Lesson 3, Ex3.4\n",
      shopping_list)


# 5. Reverse the list using sorted() method and print the list

shopping_list_reverse_sorted: list = sorted(shopping_list, reverse=True)
print("Lesson 3, Ex3.5\n",
      shopping_list_reverse_sorted)
