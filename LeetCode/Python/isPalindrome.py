#Idea = have a pointer on either end of the string and see if each one matches
        # ""
        # :type x: int
        # :rtype: bool
        # ""
def isPalindrome(x):
    int_string = str(x)
    length = int(len(int_string)/2)
    for index in range(length):
        first_char = int_string[index]
        second_char = int_string[len(int_string)-1 - index]
        if first_char is not second_char:
            return False  
    return True

num = 1001
print(isPalindrome(num))
              
