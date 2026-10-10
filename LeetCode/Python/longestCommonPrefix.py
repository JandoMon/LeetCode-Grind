        # """
        # :type strs: List[str]
        # :rtype: str
        # """
#idea sort the list and grab the smallest string. then compare that string to the rest 
def longestCommonPrefix(strs):
    prefix = ''
    strs.sort()
    small_word = strs[0] 
    for j in range(len(small_word)):
        for i in range(1,len(strs)):
            if strs[i][j] != small_word[j]:
                return prefix
        prefix += small_word[j]
    return prefix

string_list = ["flower","flow","flight"]
print(longestCommonPrefix(string_list))
