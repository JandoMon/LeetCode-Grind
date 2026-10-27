        # """
        # :type digits: List[int]
        # :rtype: List[int]
        # """

def plusOne(digits):

    #phase one
    mult = len(digits)-1
    total = 0
    for i in range(len(digits)):
        total += digits[i] * (10**mult)
        mult-=1
    total += 1 
    total = str(total)

    new_digit = []
    #phase two
    for i in range(len(total)):
        new_digit.append(int(total[i]))
    return new_digit

num = [1,2,3]
print(plusOne(num))