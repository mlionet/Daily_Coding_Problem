#This problem was asked by Facebook.
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

def number_of_ways(message) :
    if len(message) == 0 or len(message) == 1:
        return 1
    if int(message[0:2]) <= 26 and len(message[0:2]) > 1 :
        return number_of_ways(message[1:len(message)]) + number_of_ways(message[2:len(message)])
    else :
        return number_of_ways(message[1:len(message)])

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
    print(number_of_ways("111")) #should give 3
    #MY TEST
    print(number_of_ways("33333")) #should give 1
    print(number_of_ways("133")) #should give 2
    print(number_of_ways("237")) #should give 2
    print(number_of_ways("1111")) #should give 5