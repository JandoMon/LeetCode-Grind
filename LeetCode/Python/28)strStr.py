        # """
        # :type haystack: str
        # :type needle: str
        # :rtype: int
        # """
#Use sliding window approach. need to adjust the boundaries
def strStr(haystack, needle):
    len_needle = len(needle)
    for i in range(len(haystack)):
        if i + len_needle-1 < len(haystack) and haystack[i:i+len_needle] == needle:
            return i
    return -1

haystack = 'dadbutsad'
needle = 'sad'
print(strStr(haystack, needle))