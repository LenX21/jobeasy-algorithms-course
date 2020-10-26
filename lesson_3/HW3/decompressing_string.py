"""
Write a function for decompressing string “a4b3c2d”
"""
from collections import Counter


def decompressing_string_counter(string):
    count_all_letters = Counter(string)
    result = tuple(f'{letter}{counter}' for letter, counter in count_all_letters.items())
    return ''.join(result)


def decompressing_string_set(string):
    letter_set = set(string)
    result_set = []
    for i in letter_set:
        count = sum((1 if i == x else 0 for x in string))
        result_set.append(f'{i}{count}')
    return ''.join(result_set)


def decompressing_string(string):
    result_count = []
    for char in string:
        if char not in result_count:
            result_count.append(char)
            count_char = sum(1 if char == x else 0 for x in string)
            result_count.append(count_char)
    return ''.join(map(str, result_count))


def decompressing_string_dict(string):
    result = {}
    for char in string:
        if char not in result:
            count = sum((1 if x in char else 0 for x in string))
            result[char] = count
    return ''.join((f'{k}{y}' for k, y in result.items()))


if __name__ == '__main__':

    print(decompressing_string_counter('ddjjkk'))
    print(decompressing_string('ddjjkk'))
    print(decompressing_string_dict('ddjjkk'))
    print(decompressing_string_set('ddjjkk'))
