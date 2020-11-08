"""
Sum and multiplication list
Enter elements from a keyboard. Calculate sum and multiplication of elements.
Print the list, calculated sum, and multiplication of elements.


Max item and index in a list
Populate a list of random numbers. Find and print the max element and the index of this element.

Sum between min and max
Find a sum of elements between min and max elements.
Min and max elements are not included.


Array Pair Sum
Largest Continuous Sum
Duplicates
Sum of odd numbers
"""
from random import randint


def random_numbers(len_random=10):
    random_len = randint(1, len_random)
    return [randint(-100, 100) for _ in range(random_len)]


# Sum and multiplication list
# Enter elements from a keyboard. Calculate sum and multiplication of elements.
def count_sum_and_multiply(num):
    sum_all = 0
    mult_all = ''
    if num:
        mult_all = 1
        for i in num:
            sum_all += i
            mult_all *= i
    # return {
    #     'Sum': sum_all,
    #     'Multiplication': mult_all,
    #     'All items': num}
    return f"Sum:\t{sum_all}\nMult.:\t{mult_all}\nAll:\t{num}"


# Max item and index in a list
def max_number_in_the_list(num):
    print(num)
    if not num:
        print(num)
        return "List can't be empty"
    max_value = num[0]
    index = 0
    max_index = num[0]
    while index < len(num):
        index += 1
        if num[index - 1] < num[index]:
            max_value = num[index]
            max_index = index
    print(max(num), num.index(max(num)))
    print(max_value, index)



if __name__ == "__main__":
    numbers = random_numbers()
    print(count_sum_and_multiply(numbers))
    max_number_in_the_list(numbers)

