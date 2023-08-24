"""
  Lesson 4: ex4.py
"""

# 1. Create a data variable which contains a list of objects
#    with following key and values:
#    {"category": "fruit", "name": "apple"}
#    {"category": "fruit", "name": "banana"}
#    {"category": "fruit", "name": "orange"}
#    {"category": "vegetable", "name": "carrot"}
#
#    Write a for loop to print out the fruits and vegetables.
data = [{"category": "fruit", "name": "apple"},
        {"category": "fruit", "name": "banana"},
        {"category": "fruit", "name": "orange"},
        {"category": "vegetable", "name": "carrot"}]

shopping_list: dict[str, list[str]] = {}

for obj in data:
    category = obj["category"]
    if category in shopping_list:
        shopping_list[category].append(obj["name"])
    else:
        shopping_list[category] = [obj["name"]]

print(shopping_list)
