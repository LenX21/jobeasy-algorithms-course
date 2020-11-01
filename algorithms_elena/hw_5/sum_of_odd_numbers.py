"""
Sum of odd numbers
Given the triangle of consecutive odd numbers:
                1
            3       5
        7      9        11
   13	 15    17    19
21    23    25     27     29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

"""

def sum_odd_numbers_for(n):
    v = n * (n-1)
    counter = 0
    res = []
    sum_odd = 0
    while counter != n:
        if v % 2 != 0:
            sum_odd += v
            counter += 1
            res.append(v)
        v += 1
    return f"{res} = {sum_odd}"


def sum_odd_numbers_slice(n):
    res = [v for v in range(n*(n-1), n*(n+1)) if v % 2 != 0]
    return f"{res} = {sum(res)}"

if __name__ == "__main__":
    print('---- Sum of odd numbers ---- ')
    print(sum_odd_numbers_slice(3))
    print(sum_odd_numbers_for(3))

