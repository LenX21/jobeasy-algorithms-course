"""
Fiboanacci
# TODO: HW: Rewrite code, which will return only needed element of Fib sequence

Zeros not for Heros
Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

"""
from random import randint


def digital_root(number):
    if not number // 10:
        return number
    return digital_root(number % 10 + digital_root(number // 10))


def remove_zero_while(num):
    left, right = divmod(num, 10)
    while not right:
        num = left
        left, right = divmod(num, 10)
    return num


def remove_zero(num):
    left, right = divmod(num, 10)
    if not left or right:
        return num
    return remove_zero(left)


# Fibonacci: All numbers in the sequence
# Fibonacci - using while
def fibonacci_while(n):
    count = 0
    n1, n2 = 0, 1
    while count < n:
        print(n1)
        sum_n1_n2 = n1 + n2
        n1, n2 = n2, sum_n1_n2
        count += 1


# Fibonacci - Recursive functions

def fibonacci_fun(number):
    if number <= 1:
        return number
    else:
        return fibonacci_fun(number - 1) + fibonacci_fun(number - 2)


def fibonacci_count(counter):
    counter_till = counter
    for i in range(counter_till):
        print(fibonacci_fun(i))


def get_random_number(start=1, end=15000) -> int:
    number_int = randint(start, end)
    print(f"Random Number is '{number_int}'")
    return number_int


if __name__ == '__main__':
    fib_number = get_random_number(end=20)
    print(f"------Fibonacci-----")
    # Fibonacci - Recursive functions
    # fibonacci_count(fib_number)
    fibonacci_while(fib_number)

    number = get_random_number()
    print('-------Numbers ending with zeros are boring------')
    print(remove_zero_while(number))
    # Remove zero - Recursive functions
    # print(remove_zero(number))
    assert remove_zero_while(-1050) == -105, f'Error, Expected result is -105' \
                                             f'\n-1050 -> -105'
    assert remove_zero_while(1450) == 145, f'Error, Expected result is 145' \
                                           f'\n1450 -> 145'
    print('-------Sum of all the digits in a number-------')
    print(digital_root(number))
    assert digital_root(132189) == 6, f'Error,Expected result is 6' \
                                      f'\n132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6'
    assert digital_root(493193) == 2, f'Error,Expected result is 2' \
                                      f'\n493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2'
