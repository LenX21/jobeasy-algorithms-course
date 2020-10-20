"""
Recursions:
 1. Fibonacci
 2. Factorial
 3. Digital root
 4. Substitute the letter
 5. Decompressing string
 6. Count char in string

"""
from random import randint
import decompressing_string as ds
import count_char_in_string as sc


# 1. Fibonacci recursion
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


def counter_fibonacci(count):
    result = []
    for i in range(count):
        result.append(fibonacci_recursion(i))
    return result


# 2. Factorial recursion
def factorial(n):
    if n <= 1:
        return n
    else:
        return n*factorial(n-1)


# 3. Digital root
def digital_root(number):
    if not number // 10:
        return number
    return digital_root(number % 10 + digital_root(number // 10))


# 4. Substitute the string (split solution)
def print_letter_split(string, letter, replacement):
    new_string = string.split(letter)
    return replacement.join(new_string)


# 5. Decompressing string
# Import one of solution from decompressing_string.py
def decompressing_string():
    print(ds.decompressing_string_dict('abracadabra'))


# 6. Count char in string
# Import one of solution from count_char_in_string
def char_counter(case_sensitivity=True):
    letter_to_test = 'a'
    text = 'AbracadabrA'
    letter_counter = sc.count_car_in_string_list_comprehensions(text, letter_to_test, case_sensitivity)
    if not case_sensitivity:
        letter_to_test = "'a' or 'A'"
    print(f"In text '{text}' letter {letter_to_test} appears '{letter_counter}' times.")


def get_random_int(start=1, end=10000):
    int_num = randint(start, end)
    print(f'Random integer number is "{int_num}"')
    return int_num


if __name__ == '__main__':
    pretty_stuff = "*"*10
    print(f'Recursions:\n{pretty_stuff}\tFibonacci recursion\t{pretty_stuff}\n')
    n = get_random_int(end=20)
    print(counter_fibonacci(n))
    print(f'\n{pretty_stuff}\tFactorial recursion\t{pretty_stuff}\n')
    n = get_random_int(end=30)
    print(factorial(n))
    print(f'\n{pretty_stuff}\tDigital root\t{pretty_stuff}\n')
    n = get_random_int()
    print(digital_root(n))
    print(f'\n{pretty_stuff}\tSubstitute the string\t{pretty_stuff}\n')
    print(print_letter_split('Helllo lollR ll', 'll', 'RR'))
    print(f'\n{pretty_stuff}\tDecompressing string\t{pretty_stuff}\n')
    decompressing_string()
    print(f'\n{pretty_stuff}\tCount char in string\t{pretty_stuff}\n')
    char_counter()
    char_counter(False)


    assert digital_root(132189) == 6, f'Error,Expected result is 6' \
                                      f'\n132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6'
    assert print_letter_split('Test e letter', 'e', '_') == 'T_st _ l_tt_r', "Error, expected result: 'T_st _ l_tt_r' "
    assert ds.decompressing_string_dict('aaaabbbccd') == 'a4b3c2d1', 'Error, expected result: "a4b3c2d1"'
    assert sc.count_car_in_string_list_comprehensions('Test e letter not E', 'e') == 4, \
        "Error. Incorrect result"
