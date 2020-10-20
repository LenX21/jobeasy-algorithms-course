"""
Recursion for Fib, factorial, digital root

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


# Fibonacci recursion
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


# Factorial recursion
def factorial(n):
    if n <= 1:
        return n
    else:
        return n*factorial(n-1)


# Digital root
def digital_root(number):
    if not number // 10:
        return number
    return digital_root(number % 10 + digital_root(number // 10))


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
