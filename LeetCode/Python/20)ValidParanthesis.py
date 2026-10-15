
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

        