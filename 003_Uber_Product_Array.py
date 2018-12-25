#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at 
#index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

#I implement a solution without division
#I suppose that the length of an array is > 1

def product_array(array) :
    if len(array) < 2:
        return None
    ignored_index = 0
    product_array = [1] * len(array)
    while ignored_index < len(array) :
        i = 0
        while i < len(array) :
            if i != ignored_index : 
                product_array[i] *= array[ignored_index]
            i += 1
        ignored_index += 1
    return product_array

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
    print(product_array([1, 2, 3, 4, 5])) #should give [120, 60, 40, 30, 24]
    print(product_array([3, 2, 1])) #should give [3, 2, 1]
    #MY TEST
    print(product_array([0, 1, 1, 1, 1])) #should give [1, 0, 0, 0, 0]
    print(product_array([-1, 1, -1, 1, -1])) #should give [1, -1, 1, -1, 1]