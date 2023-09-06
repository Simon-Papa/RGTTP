"""
  Lesson 5: ex1.py
"""

# 1. Create even() function that return "I am even!" if number is even
#    or "I am odd!" if the number is odd.

print("Lesson 5, Ex 1.1\n"
      "Create a function that tests if an integer is even or odd\n")


def even(n: int) -> str:
    if (n % 2 == 0):
        return "I am even!"
    else:
        return "I am odd!"


print(even(2), "\n")


# 2. Create safe_even() function, that will output "I am not number!" if
#    the input is not an number otherwise will work same as even()

print("Lesson 5, Ex 1.2\n"
      "Rewrite the previous fuction with safeguards against incorrect data\n")


def safe_even(n: int) -> str:
    if (type(n) != int):
        return "I am not a number!"
    elif (n % 2 == 0):
        return "I am even!"
    else:
        return "I am odd!"


print(safe_even("Not a number"), "\n")


# 3. Create a function fizz_buzz(),
#    replacing any number divisible by three with the word "fizz",
#    and any number divisible by five with the word "buzz",
#    and any number divisible by both 3 and 5 with the word "fizzbuzz",
#    and number if number is not divisible by any.

print("Lesson 5, Ex 1.3\n"
      "Create a function 'fizz_buzz', replacing any number provided with:\n"
      "'fizz' if it divisible by 3\n"
      "'buzz' if it divisible by 5\n"
      "'fizzbuzz' if it is divisible by both 3 & 5\n"
      "print the number if none of these conditions are satisfied\n")


def fizz_buzz(n: int) -> str:
    if (type(n) != int):
        return "Invalid input"
    elif (n % 3 == 0) and (n % 5 == 0):
        return "fizzbuzz"
    elif (n % 5 == 0):
        return "buzz"
    elif (n % 3 == 0):
        return "fizz"
    else:
        return str(n)


print(fizz_buzz(7), "\n")

# 4. Execute fizz_buzz() function from 1 to the 100

print("Lesson 5, Ex 1.4\n"
      "Iterate 'fizz_buzz' from 1 - 100\n")

for x in range(1, 101):
    print(fizz_buzz(x))
