"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

biography: list = ["Simon Papa", "39", "Technical Support Engineer"]

print("Hi, My name is {0}, I am {1} years old and work as a {2}"
      .format(*biography))

# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

bibliography: dict = {"title": "The Cardinal of the Kremlin",
                      "author": "Tom Clancy",
                      "publication_year": 1988}

print("The book {title} by {author} was published in\
 {publication_year}".format(**bibliography))

# I can't seem to get positional arguments working with a dict, might need
# a review session


# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

spaceship: dict = {"name": "Odyssey",
                   "type": "BC-304 Daedalus Class Battlecruiser",
                   "purpose": "planetary defence and exploration"}

print("The spaceship is called the {name}. It is a {type} used for\
 {purpose}.".format(**spaceship))
