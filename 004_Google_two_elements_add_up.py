#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

def add_up(array, sum) :
    i = 0
    while i < len(array) :
        j = 0
        while j < len(array) :
            if i != j :
                if array[i] + array[j] == sum : return True
            j += 1
        i += 1
    return False

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
    print(add_up([10, 15, 3, 7], 17)) #should return True (10 + 7 = 17)
    #MY TEST
    print(add_up([10, 15, 3, 7], 16)) #should return False
    print(add_up([1, 1, 1, 1], 3)) #should return False