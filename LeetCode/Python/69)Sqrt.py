        # """
        # :type x: int
        # :rtype: int
        # """

def mySqrt(x):
    guess = 1
    if x == 0:
        return 0
    while guess * guess <= x:
        guess +=1
    return guess-1

print(mySqrt(16))

#Optimized solution need to implement

#Binary search while performing 
# def mySqrt(self, x: int) -> int:
#     if x < 2:
#         return x
    
#     left, right = 2, x // 2
#     while left <= right:
#         mid = (left + right) // 2
#         num = mid * mid
        
#         if num == x:
#             return mid
#         elif num < x:
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     return right