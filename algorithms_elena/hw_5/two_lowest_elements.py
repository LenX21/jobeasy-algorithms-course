"""
Homework5:
    
    Name: 
        Two lowest elements in list
    
    Description:
                When given a list of elements find the two lowest elements. 
                They can be equal to each other or different.  
"""

from random import randint


def random_list_with_random_numbers(list_len=6, max_value=100, min_value=-100):
    return [randint(min_value, max_value) for _ in range(0, list_len)]


def get_lowest_number(num):
    if not num:
        return "List can't be empty"
    elif len(num) < 2:
        return 'List contains less that 2 elements'
    else:
        min_value_0, min_value_1 = [num[0], num[1]] if num[0] < num[1] else [num[1], num[0]]
        index = 3
        while index <= len(num):
            value = num[index-1]
            if min_value_0 > value:
                min_value_1 = min_value_0
                min_value_0 = value
            elif min_value_1 > value:
                min_value_1 = value
                    
            index += 1

    return f"Two lowerst numbers: {min_value_0}, {min_value_1}"


def get_lowest_numbers_sort(arr):
    try:
        mv_0, mv_1 = sorted(arr)[:2]
    except ValueError: 
        mv_0, mv_1 = None, None
    
    return f"Two lowerst numbers: {mv_0}, {mv_1}" 
    


if __name__ == "__main__":
    print('---- Two lowest numbers ----')
    num = random_list_with_random_numbers()
    print(num)
    print(get_lowest_number(num))
    print(get_lowest_numbers_sort(num))
