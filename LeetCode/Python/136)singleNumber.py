        # """
        # :type nums: List[int]
        # :rtype: int
        # """    

def singleNumber(nums):
    seen = {}

    for num in nums:
        seen[num] = seen.get(num, 0) + 1

    for num, count in seen.items():
        if count == 1: 
            return num 
    return seen 

nums = [2,2,1] 
print(singleNumber(nums))


# #It accepted my answer but my answer is not constant space?
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res = 0

#         for n in nums:
#             res ^= n
        
#         return res
        