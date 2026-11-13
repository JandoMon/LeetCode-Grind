        # """
        # :type nums: List[int]
        # :rtype: int
        # """    

def singleNumber(nums):
    seen = {}

    for num in nums:
        if num  not in seen:
            seen[num] += 1
            
        