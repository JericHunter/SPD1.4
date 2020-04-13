"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
"""
class Solution:
    def getFib(self, N):
        # if N is less than or equal to the 1 we can just return N
        # F(0) is just 0 and same with F(1) = 1
        if N <=1:
            return N
        # otherwise call our function recursively so we can continously get our sum of N until we reach our base cases
        else:
            return self.getFib(N-1) + self.getFib(N-2)
        # this algo will have a tc of O(2^n)

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class SolutionII:
    #  Test Case:
    # [3, 5, -4, 8, 11 ,1 , -1 ,6]
    def twoSum(self,nums, targetSum):
        # Brute force solution with a tc of O(n^2)
    	for i in range(len(nums) - 1):
    		firstNum = nums[i]
    		for x in range(i+1, len(nums)):
    			secondNum = nums[x]
            # we are looping through the array looking to see if we can find a match for our target sum
    			if firstNum + secondNum == targetSum:
            # if they equal the target sum then return their indexes to find your answer given that you have a test case
    				return [i, x]
    	return []
