"""
    Homework 5:
    1. Sum of odd numbers
    2. Duplicates
    3. Below the arithmetical mean
    4. Two lowest elements in list  

"""
import random
import arithmetical_mean
import duplicates
import homework_5
import sum_of_odd_numbers
import two_lowest_elements


duplicates_solution = (
        'remove_duplicates', 
        'remove_duplicates_set',
        'remove_duplicates_list_compr',
        'remove_duplicates_enum'
    )

def get_random_list(min_value=-100, max_value=100, min_length = 1, max_length=10):
    return [random.randint(min_value, max_value) for _ in range(min_length, max_length)]


def print_odd_numbers(num):
    for i in range(1, num+1):
        row = [x for x in range(i*(i-1), i*(i+1)) if x % 2 != 0]
        print(" "*(num-i) + ' '.join(map(str, row)))


def ramdom_duplicates_func(param):
    dup_fun = random.choice(duplicates_solution)
    if dup_fun in duplicates.__dict__:
        f = duplicates.__dict__[dup_fun]
    return f(param)


def do_you_need_random_list():
    if input('Would you like to use random numbers(y/n): ') == 'y':
        arr = get_random_list()
    else:
        count = int(input('Enter amount of elemetnts in list: '))
        arr = enter_list(count)
    return arr


def enter_list(n):
    res = []
    for _ in range(n):
        res.append(int(input('enter a number: ')))
    return res


if __name__ == "__main__":
    print(f"\nHomework #5:\n")
    print('---- Sum of odd numbers ----')
    if input('Would you like to use RANDOM number(y/n): ') == 'y':
        num_count_odd = random.randint(1, 50)
        print(f"Random numder: {num_count_odd}")
    else:
        num_count_odd = int(input('Enter a number: '))
    if num_count_odd <= 10:
        print_odd_numbers(num_count_odd)

    print(f"Solution 1:\n{sum_of_odd_numbers.sum_odd_numbers_for(num_count_odd)}")
    print(f"Solution 2:\n{sum_of_odd_numbers.sum_odd_numbers_slice(num_count_odd)}")

    print('\n\n\n\n---- Duplicates ----')
    arr = do_you_need_random_list()
    print(f"initial list: {arr}")
    print(f"final result: {ramdom_duplicates_func(arr)}")

    print('\n\n\n\n---- Below the arithmetical mean ----')
    arr = do_you_need_random_list()
    print(f"initial list: {arr}")
    print(f"final result: {arithmetical_mean.arithmetical_mean_list_compr(arr)}")

    print('\n\n\n\n---- Two lowest elements in list ----')
    arr = do_you_need_random_list()
    print(f"initial list: {arr}")
    print(f"final result: {two_lowest_elements.get_lowest_numbers_sort(arr)}")
    
