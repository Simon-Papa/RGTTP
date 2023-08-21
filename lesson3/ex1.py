"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Add banana to a shopping list.

shopping_list.append('banana')
print("Lesson 3, Ex 1.1\n"
      "Shopping List appended with Banana\n")

for x in shopping_list:
    print(x)
print("\n")

# 2. Add chocolate in the third position in your shopping list

shopping_list.insert(2, 'chocolate')
print("Lesson 3, Ex1.2\n"
      "Shopping List with Chocolate inserted after Milk\n")

for x in shopping_list:
    print(x)
print("\n")


# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

shopping_list.extend(['chocolate', 'carrot', 'avocado'])
print("Lesson 3, Ex1.3\n"
      "Shopping List extended with Chocolate, Carrot and Avocado\n")

for x in shopping_list:
    print(x)
print("\n")


# 4. Remove first chocolate only


shopping_list.remove('chocolate')
print("Lesson 3, Ex1.4\n"
      "Shopping List with Chocolate removed\n")

for x in shopping_list:
    print(x)
print("\n")


# 5. Remove last item from the list

shopping_list.pop()
print("Lesson 3, Ex1.5\n"
      "Shopping List with last item removed (Avocado)\n")

for x in shopping_list:
    print(x)
print("\n")


# 6. Remove third item from the list

shopping_list.pop(2)
print("Lesson 3, Ex1.6\n"
      "Shopping List with third item removed (Bread)\n")

for x in shopping_list:
    print(x)
print("\n")

# 7. Count how many carrots are in the shopping list?

quantity: int = shopping_list.count('carrot')
print("Lesson 3, Ex1.7\n"
      "How many times is 'carrot' listed?\n")

print("Carrot is listed", quantity, "times\n")

# 8. Get the index of the chocolate (careful can throw traceback)

pos_choc: int = shopping_list.index('chocolate')
print("Lesson 3, Ex1.8\n"
      "What is the position of Chocolate in the list?\n")

print("Chocolate is listed at position", pos_choc, "\n")


# 9. Get the index of carrot, make sure this code is executed

pos_carrot: int = shopping_list.index('carrot')
pos_carrot_a: int = shopping_list.index('carrot', pos_carrot + 1)
print("Lesson 3, Ex1.9\n"
      "What is the position of Carrot in the list?\n")

print("Carrot is listed at positions", pos_carrot, "&", pos_carrot_a, "\n")
