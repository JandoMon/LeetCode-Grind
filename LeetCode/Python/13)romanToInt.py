#         """
#         :type s: str
#         :rtype: int
#         """

#Idea: Put everything into a hashmap and then grab the according value while implementing the rules
def romanToInt(s):
    roman_val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    last_seen = 'M'
    sum = 0
    for char in s:
        if roman_val[last_seen] < roman_val[char]:
            sum -= roman_val[last_seen]
            sum += roman_val[char] - roman_val[last_seen]
        else:
            sum += roman_val[char]
        last_seen = char      
    return sum

roman_string = "LVIII"
print(romanToInt(roman_string))


# • Intuitive Logic: It checks if a smaller numeral precedes a larger numeral (like I before V). If it does, it subtracts; otherwise, it adds.
# • Optimal Efficiency: Left-to-Right Look-Ahead
#                       Look-Ahead Subtraction
# 	• Time Complexity: \(O(N)\) — It inspects each character exactly once.
# 	• Space Complexity: \(O(1)\) — The memory remains perfectly constant.
# • No Double Math: Unlike your original approach, this handles subtractive pairs (like IV or XC) in a single pass without needing to undo or overwrite a previous addition.
