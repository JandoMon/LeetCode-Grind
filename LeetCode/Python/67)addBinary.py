        # """
        # :type a: str
        # :type b: str
        # :rtype: str
        # """


def addBinary(a, b):

    new_int = []
    overflow = 0
    index_a = len(a)-1
    index_b = len(b)-1

    #General Logic and Loop
    while index_a > -1 and index_b > -1:
        num_one = int(a[index_a]) 
        num_two = int(b[index_b])
        total = num_one + num_two + overflow
        new_int.insert(0,total%2)
        #Decide if there is a overflow
        if total > 1:
            overflow = 1 
        else:
            overflow = 0
        index_a -= 1
        index_b -= 1

    #Check to see if any of index a is left
    while index_a > -1:
        num_one = int(a[index_a]) 
        total = num_one + overflow
        if total > 1:
            overflow = 1
        else:
            overflow = 0
        new_int.insert(0,total%2)

    #Check to see if any of index b is left
    while index_b > -1:
        num_two = int(b[index_b]) 
        total = num_two + overflow
        if total > 1:
            overflow = 1
        else:
            overflow = 0
        new_int.insert(0,total%2)

    if overflow == 1 and index_a < 0 and index_b < 0:
        new_int.insert(0,1)
    return new_int


nums_1 = "1010"
nums_2 = "1011"
print(addBinary(nums_1, nums_2))


# The Universal Blueprint (Mental Model)
# I need to look into this more optimized solution

# 1. Initialize: Place pointers at the end of both strings (i and j), and start a carry = 0.
# 2. Loop Condition: Keep going as long as i >= 0 OR j >= 0 OR carry > 0.
# 3. Accumulate: At each step, start a sum = carry.
# 	• If i is valid, add the digit and decrement i.
# 	• If j is valid, add the digit and decrement j.
# 4. Calculate: The new digit is sum % 2 (or % 10 for decimal). The new carry is sum / 2 (integer division).
# 5. Collect & Reverse: Append the digit to a collection, and reverse it at the end.

#this is my day after halloween... gimmie a break... i am going through it... 
#I received bad news at work :(