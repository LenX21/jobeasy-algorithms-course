"""
Write a Python program to get the largest number from a input.

Count odd and even numbers.  Count odd and even digits of the whole number.

Sum of 3 modified
"""


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


def digit_number(num):
    if num // 10 == 0:
        return num
    else:
        return num % 10 + digit_number(num // 10)


def enter_a_number() -> int:
    number = None
    while not number:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Number should be integer")
    return number


if __name__ == '__main__':
    print("---largest number from a input---")
    print(find_max_number())
    print("---count odd and even numbers---")
    odd_or_even_numbers()
    print("---sum of 3 modified---")
    print(digit_number(enter_a_number()))
