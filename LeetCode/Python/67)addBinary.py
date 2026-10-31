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