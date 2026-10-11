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

#Vertical scanning
# No matter the language, the mental model is always a simple grid:
# 1. Take the first word as your baseline target.
# 2. Loop through each character position (column index col) of that first word.
# 3. Check the same column index across every other word (row index row).
# 4. Stop immediately if the row runs out of letters OR the letters don't match.

