"""
Variable assigned
a = int('Input value a')
b = int('Input value b')
print (f"a = {a} and b = {b}")

c = b
b = a
a = c
# 2 way
a = a + b
b = a - b
a = a - b

# 3 way:
a, b = b, a
"""

import math


def replace_a_with_b():
    a = int(input('Input value a: '))
    b = int(input('Input value b: '))

    c = b
    b = a
    a = c
    #
    a = a + b
    b = a - b
    a = a - b
    #
    a, b = b, a
    print(f"a = {a} and b = {b}")


"""

Sum of three digit numbers:

n = 345

for digit_number in str(n):
    sum_number += int(digit_number)
print(sum_number)

once = n % 10 
# 5

"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def digit_number_sum():
    num = int(input('Input value: '))
    sum_value = 0
    for digit_num in str(num):
        sum_value += int(digit_num)
    return sum_value

def enter_a_number() -> int:
    number = None
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Number should be integer")
    return number


def digit_number_2(num):
    if num // 10 == 0:
        return num
    else:
        return num % 10 + digit_number_2(num // 10)


def find_max_number() -> int:
    print('Enter some numbers...\nWhen you are ready type "done"')
    max_number = None
    while True:
        try:
            num = int(input("input a numbers: "))
            if max_number:
                if num > max_number:
                    max_number = num
            else:
                max_number = num

        except ValueError:
            print("Input completed")
            break
    print(f"Max value is {max_number}")
    return max_number


def odd_and_even_numbers(num):
    while num // 10 != 0:
        print(num % 10)
        num = num // 10
    print(num)


def odd_or_even_numbers():
    num = input('Enter a number:')
    odd, even, other = '', '', ''
    for i in num:
        if i.isdigit():
            if int(i) % 2 == 0:
                odd += i
            else:
                even += i
        else:
            other += i
    print(f"Odd:\t{odd}\nEven:\t{even}\n¯\_(ツ)_/¯ {other}")


def odd_or_even():
    num = input("Enter number here: ")
    odd, even, other = '', '', ''
    for i in num:
        try:
            if int(i) % 2 == 0:
                odd += i
            else:
                even += i
        except ValueError:
            other += i
    print(f"Odd:\t{odd}\nEven:\t{even}\n¯\_(ツ)_/¯ {other}")


if __name__ == '__main__':
    # print("---Factorials---")
    # n = int(input('Input Find Factorials for: '))
    # print(factorial(n))
    # print("Math factorials:")
    # print(math.factorial(n))
    # print('---Swap a and b---')
    # replace_a_with_b()
    # print('---Digit number---')
    # # print(digit_number_sum())
    # print(digit_number_2(1235))
    # find_max_number()
    # print(odd_and_even_numbers(123456789))
    odd_or_even_numbers()
    odd_or_even()

