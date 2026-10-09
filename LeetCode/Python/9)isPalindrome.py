#Idea = create a reversed version of the integer
        #Mathematical (No-String) Reversing Half Logic.
        #Base Cases:
        #   Check for Negative, (Check for Numbers ending in Zero and Check for '0' solution) makes it false
        #Loop: 
        #   Create a reversed_int var  
        #   Create a while loop where it ends if x is smaller than reversed_int
        #   Do the following:  
        #       reversed_int = (reversed_int * 10) + (reversed % 10)
        #       Decrease x        x = x // 10
        #   Return if the halfs are equal (one case in which the num of digits is even and one where the number of digits is odd)

def isPalindrome(x):
    if x<0 or (x % 10 == 0 and x !=0):
        return False
    reversed_int = 0
    while x > reversed_int:
        reversed_int = (reversed_int * 10) + (x%10)
        x = x//10
    return x == reversed_int or x == reversed_int//10
num = 1001
print(isPalindrome(num))
              
