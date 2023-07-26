"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

print("I am really enjoying the {} IDE experience".format("VS Code"))

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

print("{1} {0}".format("Panic", "Don't"))

# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

print("{name} is really {adjective}".format(name="Simon", adjective="great"))
