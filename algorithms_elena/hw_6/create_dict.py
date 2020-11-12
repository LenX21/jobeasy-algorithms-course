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


def create_dict_way1(arr1, arr2):
    joined_dict = {k: None for k in arr1}
    for k, v in zip(arr1, arr2):
        joined_dict[k] = v
    return joined_dict


def create_dict_way2(arr1, arr2):
    return {k: v for k, v in itertools.zip_longest(arr1, arr2, fillvalue=None)}


def create_dict_way2_ext(*lists):
    def g(lists):
        for item in lists:
            if item:
                yield lists
            yield None

    gen = [g(l) for l in lists]
    for _ in range(max(map(len, lists))):
        print(tuple(x for x in next(gen)))


list_all = ([1, 2, 3, 4], ['a', 'b', 'c'])
create_dict_way2_ext(list_all)
print(create_dict_way1(*list_all))
print(create_dict_way2(*list_all))