"""
  Lesson 5: ex4.py
"""

# 1. Write a function get_index() that returns the index of
#    a character in a string


def get_index(word: str, char: str) -> int:
    for index, letter in enumerate(word):
        if letter == char:
            return index


print(get_index("Red Hat", "e"))


# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.

def shout(sentence: str) -> None:
    for word in sentence.split(" "):
        print(f"{word.upper()}!")


shout("This is impressive text manipulation")

# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False


def extract_longer(n: int, sentence: str) -> list | bool:
    result: list[str] = []
    for word in sentence.split(" "):
        if (len(word) >= n):
            result.append(word)
    return result if result else False


print(extract_longer(3, "How is it going?"))
