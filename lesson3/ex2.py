"""
  Lesson 3: ex2.py
"""

# 1. Create a list of number 0 to 9 using a for loop.
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num_list: list[int] = [i for i in range(10)]
print("Lesson 3, Ex2.1\n",
      num_list)


# 2. Create a list of number from 0 to 9 the power of 2 using a for loop.
#
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

num_list_sqrd: list[int] = [i**2 for i in range(10)]
print("Lesson 3, Ex2.2\n",
      num_list_sqrd)


# 3. Create a list of lists, which contains elements that are
# number, number(to the power of 2), number(to the power of 3)
#
# [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64],
#  [5, 25, 125], [6, 36, 216], [7, 49, 343], [8, 64, 512],
#  [9, 81, 729]]

num_list_cubed: list = [[i, i**2, i**3] for i in range(10)]
print("Lesson 3, Ex2.3\n",
      num_list_cubed)


# 4. Add condition in a for loop, that only numbers that are odd are added.
#
# [[1, 1, 1], [3, 9, 27], [5, 25, 125], [7, 49, 343], [9, 81, 729]]

num_list_odd: list = [[i, i**2, i**3] for i in range(10) if i % 2]
print("Lesson 3, Ex2.4\n",
      num_list_odd)


# 5. Create a nested lists in a list with a for loop:
# [['ax', 'bx', 'cx', 'dx', 'ex'],
#  ['ay', 'by', 'cy', 'dy', 'ey'],
#  ['az', 'bz', 'cz', 'dz', 'ez']]

nested_list: list = [[i+j for i in 'abcde'] for j in 'xyz']
print("Lesson 3, Ex2.5\n",
      nested_list)
