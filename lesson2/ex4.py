"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

for x in versions:
    print("{:<10}".format(x), "{}".format(versions[x]))

# 2. Print {} around the version numbers.

for x in versions:
    print("{:<10}".format(x), "{{{}}}".format(versions[x]))

# INSERT YOUR CODE HERE

# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE
for x in versions:
    print("{:<10}".format(x), "{:>6b} binary".format(versions[x]))
    print("{:<10}".format(x), "{:>6o} octal/byte".format(versions[x]))
    print("{:<10}".format(x), "{:>6} decimal".format(versions[x]))
    print("{:<10}".format(x), "{:>6x} hex".format(versions[x]))

# Wasn't sure about byte vs binary so I did both
