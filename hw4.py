"""Given a list of n numbers, determine if it contains any duplicate numbers."""

# create a dictionary
# loop through num list
# loop through items in dict

# O(n)
def contains_duplicates(nums):
	duplicates = {}
	for element in nums:
		if element in duplicates:
			duplicates[element] +=1
		else:
			duplicates[element] = 1
	for item in duplicates.items():
		if duplicates[item] > 1:
			print item
