#Variables: create hash map of the correct opening for every closing. 
#           create an empty stack
#Logic/Loop:
#       for every index in the list:
#           Do the following: 
#               if the current value is a opening 
#                   add it to the stack
#               else 
#                   check to see that the stack is not empty or 
#                   check to see if the top of the stack matches the key/value pair of the current closing value
#                       if either conditions is true, then return false
#       return if the stack is empty or not (true/false)
#         """
#         :type s: str
#         :rtype: bool
#         """
def isValid(s):
    brackets = { ']':'[', ')':'(', '}':'{' }
    stack = []

    for index in range(len(s)):
        if s[index] == '[' or s[index] == '{' or s[index] == '(':
            stack.append(s[index])
        else:
            if not stack or stack.pop() != brackets.get(s[index]):
                return False
    return not stack 


para = "([])"
para2 = "([)]"
para3 = "]"
print(isValid(para3))

        