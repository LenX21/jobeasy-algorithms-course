"""
Find and replace a substring in a string for another substring.
User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE
"""


def replace_char(string, letter, letter_replace):
    if len(letter) == 1:
        result = tuple(letter_replace if i in letter else i for i in string)
        return ''.join(result)


def print_letter_find(string, letter, replacement):
    count = len(letter)
    position = string.find(letter)
    while position != -1:
        string = string[0:position] + replacement + string[position+count:]
        position = string.find(letter)
    return string


def print_letter_split(string, letter, replacement):
    new_string = string.split(letter)
    return replacement.join(new_string)


print(print_letter_find('Hello lolltt ll', 'l', 'R'))
print(print_letter_split('Helllo lollR ll', 'll', 'RR'))
print(print_letter_find('Helllo lolltt ll', 'll', 'RR'))
print(print_letter_split('Helllo lollR ll', 'll', 'RR'))