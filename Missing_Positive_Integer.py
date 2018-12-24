#This problem was asked by Stripe.
#Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place

def get_positive_array(array) :
    positives = []
    for element in array :
        if element > 0 :
            positives.append(element)
    return positives

def sort_array(array) :
    i = 0
    while i < len(array) - 1 :
        if array[i] > array[i + 1] :
            tmp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = tmp
            i = 0
        else :
            i += 1

def missing_integer(array) :
    positives = get_positive_array(array)
    if len(positives) == 0 :
        return 1
    if len(positives) == 1 :
        return 2 if positives[0] == 1 else 1
    sort_array(positives)
    min = 1
    for element in positives :
        if min == element : min += 1
    return min

if __name__ == '__main__' : 
    print(missing_integer([3, 4, -1, 1])) #should give 2
    print(missing_integer([1, 2, 0])) #should give 3
    print(missing_integer([2, 3, 7, 6, 8, -1, -10, 15])) #should give 1
    print(missing_integer([2, 3, -7, 6, 8, 1, -10, 15])) #should give 4
    print(missing_integer([1, 1, 0, -1, -2])) #should give 2