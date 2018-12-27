#This problem was asked by Jane Street.
#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#Given this implementation of cons:
#def cons(a, b):
#    def pair(f):
#        return f(a, b)
#   return pair
#Implement car and cdr.

def cons(a, b) :
    def pair(f) :
        return f(a, b)
    return pair

def car(f) :
    def right(a, b) :
        return a
    return f(right)

def cdr(f) :
    def left(a, b) :
        return b
    return f(left)

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))