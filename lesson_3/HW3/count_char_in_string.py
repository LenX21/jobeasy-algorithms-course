"""
Write a Python function, which will count how many times a character (substring) is included in a string.
DON’T USE METHOD COUNT
"""
from collections import Counter


def count_car_in_string_for(string, letter, letter_case_matters=True):
    count = 0
    if not letter_case_matters:
        string = string.lower()
    for i in string:
        if i == letter:
            count += 1
    return count


def count_car_in_string_list_comprehensions(string, letter, letter_case_matters=True):
    if letter_case_matters:
        return sum(tuple(1 if i == letter else 0 for i in string))
    return sum(tuple(1 if i in letter else 0 for i in string.lower()))


def count_car_in_string_list_counter(string, letter, letter_case_matters=True):
    if letter_case_matters:
        count = Counter(string)
        return count['e']
    count = Counter(string.lower())
    return count['e']


if __name__ == '__main__':
    assert count_car_in_string_for('TestHowManyTimesCharAppearsInStringABCBEFGHIJKLMNOPQ', 'e') == 3, \
        "Error. Incorrect result"
    assert count_car_in_string_for('TestHowManyTimesCharAppearsABCBEFGHIJKLMNOPQ', 'e', False) == 4, \
        "Error. Incorrect result"

    assert count_car_in_string_list_comprehensions('TestHowManyTimesCharAppearsInStringABCBEFGHIJKLMNOPQ', 'e') == 3, \
        "Error. Incorrect result"
    assert count_car_in_string_list_comprehensions('TestHowManyTimesCharAppearsABCBEFGHIJKLMNOPQ', 'e', False) == 4, \
        "Error. Incorrect result"

    assert count_car_in_string_list_counter('TestHowManyTimesCharAppearsInStringABCBEFGHIJKLMNOPQ', 'e') == 3, \
        "Error. Incorrect result"
    assert count_car_in_string_list_counter('TestHowManyTimesCharAppearsInStringABCBEFGHIJKLMNOPQ', 'e', False) == 4, \
        "Error. Incorrect result"
