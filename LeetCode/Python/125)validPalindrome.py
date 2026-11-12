        # """
        # :type s: str
        # :rtype: bool
        # """

def isPalindrome(s):
    i = 0 
    r = len(s)-1
    while i < r:
        while i < len(s)-1 and not s[i].isalnum():
            i+=1
        while r > 0 and not s[r].isalnum():
            r-=1
        leftchar = s[i].lower()
        rightchar = s[r].lower()
        if i < r and leftchar != rightchar:
            return False
        i+=1
        r-=1
    return True
s = ".,"
s1 = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

#Need to find optimal solution
#will do on saturday 
