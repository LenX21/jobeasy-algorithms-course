'''
Homework 5:
    Name: Arithmetical mean

    Discription: 
        When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.  
        The arithmetical mean is the sum of all elements divided by the number of elements
'''
def arithmetical_mean(arr):
    sum_all = 0
    counter = 0
    res = []
    for i in arr:
        sum_all += i
        counter += 1
    arith_mean = sum_all / counter
  
    for i in arr:
        if i < arith_mean:
            res.append(i)
    return res


def arithmetical_mean_list_compr(arr):
    arith_mean = sum(arr) / len(arr)
    res = [x for x in arr if x < arith_mean]
    return res



if __name__ == "__main__":
    print('---- Arithmetical mean -----')
    arr = [1, 2, 3, 4, 20, 1]
    print(arr)
    print(arithmetical_mean(arr))
    print(arithmetical_mean_list_compr(arr))
    assert arithmetical_mean_list_compr ([1, 2, 3, 4]) == [1, 2] , "Error. Expected result [1, 2]"
