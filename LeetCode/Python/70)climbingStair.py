        # """
        # :type n: int
        # :rtype: int
        # """

def climbStairs(n):
    current_1, previous_2 = 1, 1
    for i in range(1,n):
        temp = current_1
        current_1 = current_1 + previous_2
        previous_2 = temp
    return  current_1
print(climbStairs(4))
        