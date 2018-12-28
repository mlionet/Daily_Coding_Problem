#This problem was asked by Airbnb.
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(array) :
    if (len(array) == 0) :
        return 0
    if (len(array) == 1) :
        return array[0]
    value1 = array[0] + largest_sum(array[2:len(array)])
    value2 = largest_sum(array[1:len(array)])
    if (value1 > value2) :
        return value1
    return value2

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
    print(largest_sum([2, 4, 6, 2, 5]))#should give 13
    print(largest_sum([5, 1, 1, 5]))#should give 10
    print(largest_sum([10, 10, 10]))#should give 20
    print(largest_sum([1, 1, 0, -1]))#should give 1
    print(largest_sum([10,0,0,9,10]))#should give 20
    print(largest_sum([2]))#should give 1