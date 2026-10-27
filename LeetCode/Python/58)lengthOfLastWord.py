        # """
        # :type s: str
        # :rtype: int
        # """

def lengthOfLastWord(s):
    count =0
    start_pointer = len(s)-1

    # Phase 1: Skip trailing spaces (Must include >= 0)
    while start_pointer >= 0 and s[start_pointer] == ' ':
        start_pointer-=1
    # Phase 2: Count the last word (Must go down to -1 to include index 0)
    for i in range(start_pointer, -1, -1):
        if s[i] != ' ':
            count+=1
        else:
            return count
    return count

word = "Hello World"
print(lengthOfLastWord(word))