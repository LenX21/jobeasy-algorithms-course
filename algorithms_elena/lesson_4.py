"""
Split in half


Given a string. Split it for two same parts. (if the string has odd characters,
the first part should be greater by one character). Swap this parts and save the result in a new string and return it.

Delete fragment

Given a string. Character “h” is included as minimal two times.
Delete from given string first and last h - characters and all characters between them.


String cleaning
Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database.
At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.
For example:
string_clean('! !') == '! !'
string_clean('123456789') == ''
string_clean('This looks5 grea8t!') == 'This looks great!'
Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers.
Your program will take in a string and clean out all numeric characters, and return a string with

Help Bob count letters and digits.
Bob is a lazy man.
He needs you to create a method that can determine how many letters and digits are in a given string.

Example:
"hel2!lo" --> 6
"wicked .. !" --> 6
"!?..A" --> 1
No duplicate

Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
Input: 'alpha beta beta gamma   gamma gamma delta alpha beta beta gamma gamma gamma delta'
Output: 'alpha beta gamma delta'

Isogram
Isogram is a word with no repeating letters, in a row or not.
Create a Python function to check is word isogram. Empty string - isogram. Case doesn’t matter.

"""
import inspect
import timeit


# Split in half
def split_in_half(s):
    return s[len(s) // 2 + 1:] + s[:len(s) // 2 + 1]


def split_in_half_round(s):
    return s[round(len(s) / 2 + 0.1):] + s[:round(len(s) / 2 + 0.1)]


def split_in_half_for_loop(s):
    w1, w2 = '', ''
    for i in range(len(s)):
        if i <= round(len(s) // 2 + 0.01):
            w1 += s[i]
            continue
        w2 += s[i]
    return w2 + w1


# Delete fragment
def delete_fragment(s, char):
    h_chars = [i for i in range(len(s)) if s[i] in char]
    print(h_chars)
    if len(h_chars) < 2:
        return None
    return s[:h_chars[0]] + s[h_chars[-1] + 1:]


def delete_fragment_for_loop(s, char):
    w = ''
    h_found = False
    for ele in s:
        if ele in char:
            h_found = not h_found
            continue
        if not h_found:
            w += ele
    return w


# String cleaning
def string_cleaning(s):
    new_s = [x for x in s if not x.isdigit()]
    return ''.join(new_s)


# Count letters and digits.
def count_letters_and_digits(s):
    new_s = [x for x in s if x.isdigit() or x.isalpha()]
    return len(new_s)


def count_letters_and_digits_sum(s):
    new_s = sum([1 for x in s if x.isdigit() or x.isalpha()])
    return new_s


# Isogram
def isogram(s):
    return len(s) == len(set(s))


def isogram_for_loop(s):
    iso = ''
    for ele in s:
        if ele in iso:
            return False
        iso += ele
    return True


# Remove all duplicate words


def time_it(func, params, comment=None, pprint=True):
    stp = inspect.getsource(func)
    run_it_times = 10000
    name = func.__name__
    stmt = f"{name}('{params}')"
    if pprint:
        print(f'Run: {stmt} {run_it_times} times\n{comment}')
    print(timeit.timeit(setup=stp, stmt=stmt, number=run_it_times))


if __name__ == "__main__":
    # String cleaning
    assert string_cleaning('This looks5 grea8t!') == 'This looks great!'
    assert string_cleaning('! !') == '! !'
    assert string_cleaning('123456789') == ''
    # Isogram
    assert isogram('dialogue') == True, "Error, Isogram set"
    assert isogram_for_loop("dialogue") == True, "Error, Isogram for loop"
    assert isogram('deed') == False
    # Count letters and digits
    assert count_letters_and_digits("hel2!lo") == 6
    assert count_letters_and_digits("wicked .. !") == 6
    assert count_letters_and_digits("!?..A") == 1
    # Delete fragment
    assert delete_fragment('11h22h33', 'h') == '1133'
    assert delete_fragment_for_loop('11h22h33', 'h') == '1133'
    # Split in half
    assert split_in_half_for_loop('test1pppp') == 'pppptest1'
    assert split_in_half_round('test1pppp') == 'pppptest1'

    print('Split in half')
    time_it(split_in_half_for_loop, 'test1pppp', comment='Split using for loop(by counting amount of items)')
    time_it(split_in_half_round, 'test1pppp', comment='Split using list slicing and round amount of items in list by '
                                                      '+ 0.01 to make first part be longer than second one')
    print('Isogram.\nIsogram is a word with no repeating letters, in a row or not.')
    time_it(isogram, 'dialogue', 'Compare amount of items. Transform string to set and compare')
    time_it(isogram_for_loop, 'dialogue', comment='use for loop. Return false as soon as find duplications')
    print('Count letters and digits')
    time_it(count_letters_and_digits, "hel2!lo", comment='Check if isalpha() and isdigit(), add them to list and '
                                                         'count amount using len()')
    time_it(count_letters_and_digits_sum, "hel2!lo",
            comment='Check if isalpha() and isdigit(), add 1 for each to list and count amount using sum()')
