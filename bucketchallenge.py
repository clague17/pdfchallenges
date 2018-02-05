from collections import *
'''
You are given an array bucket_sizes (e.g. [3, 11, 21]) and a target_value (e.g. 492).
The resulting answer should be a 1 or 0 (alternatively true and false)
1 (true) - if the buckets can be used to reach the target value
0 (false) - if they cannot
ex:

Given:
 bucket_sizes <-- [5, 7]
 target_value <-- 5
 return 1 (true)

Given:
 bucket_sizes <-- [5, 7]
 target_value <-- 33
 return 1 (true), because 5 + 7 + 7 + 7 + 7 = 33

Given:
 bucket_sizes <-- [5, 7]
 target_value <-- 9
 return 0 (false), because no combination of adding the provided bucket_sizes gives 9 as a sum; (7 + 7 - 5 = 9 is not considered a valid solution)

'''
def targetbuckets(buckets, target):
	'''
	Inputs: a list of integers, 'buckets', a combination of which must sum to the integer 'target'
	Output: True/False respectively if 'target' can be reached by strict sum  
	'''
	if not buckets and target:
		return "No target can be achieved with zero buckets!"
	if target < 0:
		return "Cant really achieve a negative target number... Try a positive!"
	if target == 0:
		return True, "a target of 0 can be achieved by everything, or is it nothing?"
	counter = 0
	maximum = len(buckets)
	while counter < maximum:
		print buckets
		print 'target:', target
		for num in buckets:
			print target,'mod',num ,'=', target%num
			if (target%num) in buckets:
				#if target doesnt perfectly divide by num, you can add another element in buckets to achieve target
				return True
			elif target%num == 0:
				#if target perfectly divides by num then its a match
				return True
		target = target - buckets[counter] #expedites the process
		counter += 1
		print counter
	return False

#test cases:
# buckets = [3,11,21]
# target = 20
# print targetbuckets(buckets, target) 
# print 95%3

# buckets = [5, 7]
# target = 5

# buckets = [5, 7]
# target = 33

# buckets = [5, 7]
# target = 9

# buckets = [1]
# target = 0
print targetbuckets(buckets, target)


