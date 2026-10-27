        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: int
        # """ 

import math

def searchInsert(nums, target):
    right = len(nums)-1
    left = 0
    while left < right:
        middle = left + (right - left)//2
        if target > nums[middle]:
            left = middle +1 
        else: 
            right = middle -1
    return left

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))