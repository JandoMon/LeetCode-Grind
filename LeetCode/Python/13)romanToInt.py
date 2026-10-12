#         """
#         :type s: str
#         :rtype: int
#         """
# Idea: check to see if a smaller number comes before a bigger one. If it does, subtract the current number otherwise add the current number
# Name: Left to Right Look-Ahead Subtraction
# Base Case: None
# Variables: Create a hashmap with the values of each roman-value pair
# Loop: For every index in the the list do the following:
# Check to see if you can even look ahead in the list, if so: check to see if the next value is greater than current
# If the condition is true: subtract the current value from the total
# If the condition is false: add the current value to the total
# return total 
def romanToInt(s):
    roman_val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    for i in range(len(s)):
        if i+1 < len(s) and roman_val[s[i]] < roman_val[s[i+1]]: 
            total -= roman_val[s[i]]
        else:
            total += roman_val[s[i]]
    return total

roman_string = "MIX"
print(romanToInt(roman_string))
