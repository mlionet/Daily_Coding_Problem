#This problem was asked by Amazon.

#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
#Given N, write a function that returns the number of unique ways you can climb the staircase.
#The order of the steps matters.

#For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

#What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
#For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def count_steps_combinations(steps, set_numbers) :
	if (steps == 0) :
		return 1
	if (len(set_numbers) == 0 or steps < 0) :
		return 0
	steps_count = 0
	for n in set_numbers :
		steps_count += count_steps_combinations(steps - n, set_numbers)
	return steps_count

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
	print(count_steps_combinations(4, [1, 2]))#Should give 5
	#MY TEST
	print(count_steps_combinations(4, [1]))#Should give 1
	print(count_steps_combinations(3, [1, 2, 3]))#Should give 4
	print(count_steps_combinations(3, [4]))#Should give 0
	print(count_steps_combinations(5, [2, 3, 5]))#Should give 3