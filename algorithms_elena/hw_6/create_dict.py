"""Create dictionary
    There are two lists that have different length. First has keys and the second has values.
    Create a function, which creates a dictionary of keys and values.
    If the is not enough values to match each key, this key should have value equal to None.
    If the is not enough keys to match each value, this value should be ignored.
"""


# Way 1: Create dict with None values and then fill data. What's left stays as None
# Way 2: Use zip_longest python module
# Way 2 extended: Use zip_longest approach. Return None till it requested
import itertools
import timeit
import inspect

def create_dict_way1(arr1, arr2):
    joined_dict = {k: None for k in arr1}
    for k, v in zip(arr1, arr2):
        joined_dict[k] = v
    return joined_dict


def create_dict_way2(arr1, arr2):
    return {k: v for k, v in itertools.zip_longest(arr1, arr2, fillvalue=None)}


def create_dict_way2_ext(*lists):
    def g(lst):
        for item in lst:
            yield item
        while True:
            yield None
    dict_none = {}
    gen_k = g(lists[0])
    gen_v = g(lists[1])
    for _ in range(max(map(len, lists))):
        dict_none[next(gen_k)] = next(gen_v)
    return dict_none


def time_it(func, prams):
    stp = inspect.getsource(func)
    name = func.__name__
    stmt = f'{name}({prams})'
    print("{:60} : {}".format(
        stmt,
        timeit.timeit(setup=stp, stmt=stmt, number=10000)))


if __name__ == "__main__":
    list_all = ([1, 2, 3, 4], ['a', 'b', 'c'])
    print(create_dict_way2_ext(*list_all))
    print(create_dict_way1(*list_all))
    print(create_dict_way2_ext(*list_all))
    print(' ------------ Time it ------------------')
    list_all_str = ", ".join((repr(x) for x in list_all))
    time_it(create_dict_way1, list_all_str)
    time_it(create_dict_way2, list_all_str)
    time_it(create_dict_way2_ext, list_all_str)

