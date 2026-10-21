        # """
        # :type nums: List[int]
        # :rtype: int
        # """

#Idea: use a double pointer system to not only iterate through the list but to keep track of where to add the unique elements
#Lopic/Loop: 
#   create a variable called unique 
#   use a for loop to go to every index of the list
#   Do the folllowing: 
#       if the number is not equal to the last item in the unique list
#       add it to the list and update the index of the last unique item

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