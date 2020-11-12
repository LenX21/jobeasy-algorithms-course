"""
Divide and rule I
    You have a list of numbers. You should sum up all numbers and output their sum.
"""
def divide_rule_res(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        middle = len(arr) // 2
        left, right = arr[:middle], arr[middle:]
        result = sum(left) + sum(right)
        result += divide_rule_res(left)
        result += divide_rule_res(right)
        return result


def divide_rule_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        middle = len(arr) // 2
        left, right = arr[:middle], arr[middle:]
        result_l = divide_rule_max(left)
        result_r = divide_rule_max(right)
        return max(result_l, result_r)


if __name__ == "__main__":
    print('-----------Divide and rule I----------------')
    print(divide_rule_res([1, 2, 3, 4, 5, 6, 7, 8]))

    print('---------Max value from that list------------')
    print(divide_rule_max([1, 2, 3, 4, 5, 6, 7, 8]))