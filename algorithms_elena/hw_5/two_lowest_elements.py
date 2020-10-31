from random import randint


def random_list_with_random_numbers(list_len=6, max_value=100, min_value=-100):
    return [randint(min_value, max_value) for _ in range(0, list_len)]


def get_lowest_number(num):
    if not num:
        return "List can't be empty"
    elif len(num) < 2:
        return 'List contains less that 2 elements'
    else:
        min_value_0, min_value_1 = '', ''
        index = 1
        while index < len(num):
            if min_value_0:
                if min_value_0 > num[index-1]:
                    min_value_1, min_value_0 = min_value_0, num[index-1]
            else:
                if num[index] > num[index-1]:
                    min_value_0 = num[index-1]
                    min_value_1 = num[index]
            index += 1

    return f"Two lowerst numbers: {min_value_0}, {min_value_1}"



if __name__ == "__main__":
    num = random_list_with_random_numbers()
    print(num)
    print(get_lowest_number(num))
