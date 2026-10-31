        # """
        # :type digits: List[int]
        # :rtype: List[int]
        # """

def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        #if current digit is less than 9, add one and return early
        if digits[i] < 9:
            digits[i] += 1
            return digits
        ## If it's 9, it becomes 0 (carry over to the next left digit)
        digits[i] = 0
    # If the loop finishes, it means the number was all 9s (e.g., [9, 9, 9] ->)
    return [1] + digits

num = [1,2,3]
print(plusOne(num))