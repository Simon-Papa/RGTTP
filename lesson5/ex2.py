"""
  Lesson 5: ex2.py
"""

# 1. Write a while true loop to print "Forever" forever

# while True:
#     print("Forever")

# 2. Write a while loop to print numbers from 0 to 42

x: int = 0
while (x <= 42):
    print(x)
    x += 1

# 3. Write a while true loop to print numbers from 0 to 42

y: int = 0
while True:
    if (y > 42):
        break
    print(y)
    y += 1

# 4. Write a while true loop to print numbers from 0 to 45, and instead
#    of 42, print "I am 42!" break at number 45.

z: int = 0
while True:
    if (z > 45):
        break
    elif (z == 42):
        print("I am 42!")
        z += 1
        continue
    print(z)
    z += 1

# 5. Write a while-else loop to count to 2, and after that print
#    "It's my turn now!" using else statement.

n: int = 0
while (n <= 2):
    print(n)
    n += 1
else:
    print("It's my turn now!")
