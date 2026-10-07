#Idea: Search for the compliment in the list
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]

#Solution:
# Find the compliment of each item in the list and see if it is in the hashmap (i.e. dictionary) 
# of seen{} return the solution
def two_sums(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        compliment = target - num
        if compliment in seen: 
            return [seen[compliment], index]
        seen[num] = index

test_list = [2,7,11,15]
print(two_sums(test_list,9))