"""Given a non-empty array of integers, every element appears twice except for one. Find that single one."""

class Solution(object):
    def singleNumber(self, nums):
        no_duplicates = []
        for i in nums:
            if i not in no_duplicates:
                no_duplicates.append(i)
            else:
                no_duplicates.remove(i)
        return no_duplicates.pop()

#Time complexity : O(n^2) We search the whole list to find whether there is duplicate number, taking O(n)time.
#Because search is in the for loop, we have to multiply both time complexities which is O(n^2).
