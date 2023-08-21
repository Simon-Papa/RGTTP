"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

name: str = "Simon"
age: int = 39

print("Hi, my name is {0} and I am {1} years old".format(name, age))

# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

pseudonym: dict = {"RHSOP10": "Newton",
                   "RHOSP13": "Queens",
                   "RHOSP16.x": "Train",
                   "RHOSP17": "Wallaby"}

print("Here is a list of Red Hat Openstack versions and the Upstream projects"
      "that they were based on:\n")

for x in pseudonym:
    print("{:<10}".format(x), "{:>15}".format(pseudonym[x]))

# 3. Show different representations of an integer.

number_a: int = -3
number_b: int = 6
number_c: int = number_a + number_b
print("{:+} + {:+} = {:+}".format(number_a, number_b, number_c))
print("{:-} + {:-} = {:-}".format(number_a, number_b, number_c))


# 4. Format a floating-point number with fixed precision.

number_d: float = 56
print("{:.2f}".format(number_d))
