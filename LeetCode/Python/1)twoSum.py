#prompt to find the best solution: 
#what approach should I use to solve this problem across as many languages to help me remember
#what is the most efficient way to sovle this problem across as many languages
#what should i call this logic solution to help me remember
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

test_list = [2,15,11,7]
print(two_sums(test_list,9))


# The Universal Blueprint (Mental Model)
# I need to look into this more optimized solution

# 1. Initialize: Place pointers at the end of both strings (i and j), and start a carry = 0.
# 2. Loop Condition: Keep going as long as i >= 0 OR j >= 0 OR carry > 0.
# 3. Accumulate: At each step, start a sum = carry.
# 	• If i is valid, add the digit and decrement i.
# 	• If j is valid, add the digit and decrement j.
# 4. Calculate: The new digit is sum % 2 (or % 10 for decimal). The new carry is sum / 2 (integer division).
# 5. Collect & Reverse: Append the digit to a collection, and reverse it at the end.