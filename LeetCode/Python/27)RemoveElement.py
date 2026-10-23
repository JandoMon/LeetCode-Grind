#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
def removeElement(nums, val):
    curr = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[curr] = nums[i]
            curr+=1
    return curr

nums_ = [3,2,2,3]
print(removeElement(nums_, 3))