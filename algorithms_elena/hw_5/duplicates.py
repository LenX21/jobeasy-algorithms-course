"""
Homework 5:
    Name: Duplicates
    
    Description: Write a Python program to remove duplicates from a list.

Methods to solve it:
    1. Set
    2. Enumerate 
    3. For loop

"""
import timeit
import inspect


def remove_duplicates(arr):
    no_dup = []
    for ele in arr:
        if ele in no_dup:
            continue
        no_dup.append(ele)
    return no_dup


def remove_duplicates_set(arr):
    return list(set(arr))


def remove_duplicates_list_compr(arr):
    res =[]
    [res.append(x) for x in arr if x not in res]
    return res


def remove_duplicates_enum(arr):
    res = [i for n, i in enumerate(arr) if i not in arr[:n]]
    return res


def time_it(func, param):
    stp = inspect.getsource(func)
    name = func.__name__
    stmt = f'{name}("{param}")'
    print(timeit.timeit(setup=stp, stmt=stmt, number=10000))


if __name__ == "__main__":
    print('---- Remove Duplicates ---- ')
    arr = [1, 1, 2, 3, 't', 't', 45]
    print(remove_duplicates(arr))
    print(remove_duplicates_set(arr))
    print(remove_duplicates_list_compr(arr))
    print(remove_duplicates_enum(arr))
    print('---- Find what is the fasters way to solve it ----')
    time_it(remove_duplicates, arr)
    time_it(remove_duplicates_set, arr)
    time_it(remove_duplicates_list_compr, arr)
    time_it(remove_duplicates_enum, arr)
    print('----')

