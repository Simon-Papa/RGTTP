"""
  Lesson 5: ex3.py
"""

# 1. Write a for loop to iterate over list: [1, 2, 3, 'a', 'b', 'c']

for i in [1, 2, 3, 'a', 'b', 'c']:
    print(i)

# 2. Write for loop to print each character in word "orange"

for a in "orange":
    print(a)

# 3. Using following shopping list:
# shopping_list: ['orange', 'banana', 'mandarin']
# Print "Note to self, buy: " and then iterate
# over each element in the list

shopping_list: list[str] = ["orange",
                            "banana",
                            "mandarin"]

for x in shopping_list:
    print("note to self, buy:", x)

# 4. Write for loop using range to print numbers from 0 to 10

for k in range(1, 11):
    print(k)

# 5. Write for loop using range to print numbers from 10 to 20

for p in range(10, 21):
    print(p)

# 6. Write for loop using range to print even numbers from 10 to 20

for m in range(10, 21):
    if (m % 2 == 0):
        print(m)

# 7. Write for loop using range, to print every 5 numbers
#    down from 100 to 0

for n in range(100, 0, -5):
    print(n)

# 8. Write for loop using enumerate to print element and it's index

for index, item in enumerate(shopping_list):
    print(f"{index}. {item}")
