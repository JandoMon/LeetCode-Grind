        # """
        # :type nums: List[int]
        # :rtype: int
        # """
#Idea: use a double pointer system to not only iterate through the list but to keep track of where to add the unique elements

def removeDuplicates(nums):
    unique = 1
    if not nums:
        return 0
    unique = 1
    for i in range(1,len(nums)):
        if nums[unique-1] != nums[i]:
            nums[unique] = nums[i]
            unique += 1
    return unique

num_list = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(num_list), num_list) 