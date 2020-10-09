"""
Write a Python program to get the largest number from a input.

Count odd and even numbers.  Count odd and even digits of the whole number.

Sum of 3 modified
"""

from random import randint


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


def odd_or_even_numbers(num):
    odd, even = 0, 0
    left = num // 10
    right = num % 10
    if right:
        if right % 2 == 0:
            even = 1
        else:
            odd = 1
    if left != 0:
        temp = odd_or_even_numbers(left)
        odd += temp[0]
        even += temp[1]
    return odd, even


def count_even_and_odd(num):
    # print(f"Number is '{num}'")
    odd, even = odd_or_even_numbers(num)
    print(f"Odd:\t{odd}\nEven:\t{even}")


def digit_number(number):
    if number // 10 == 0:
        return number
    else:
        return number % 10 + digit_number(number // 10)


def enter_a_number() -> int:
    number = None
    while not number:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Number should be integer")
    return number


def get_random_number(start=0, end=10000):
    return randint(start, end)


if __name__ == '__main__':
    num = get_random_number()
    print(f"Random integer: '{num}'")
    print("---largest number from a input---")
    print(find_max_number())
    print("---count odd and even numbers---")
    count_even_and_odd(num)
    print("---sum of 3 modified---")
    print(digit_number(num))
