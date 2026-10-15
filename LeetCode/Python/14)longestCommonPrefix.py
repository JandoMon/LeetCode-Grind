        # """
        # :type strs: List[str]
        # :rtype: str
        # """
#idea sort the list and grab the smallest string. then compare that string to the rest 
def longestCommonPrefix(strs):
    if not strs:
        return ''

    #use first word as the template
    reference = strs[0]

    for index_first_word in range(len(reference)):
        char = reference [index_first_word]

        # Check this character postion against all other strings
        # Early Exit: If another word is shorter than 'i'
        # or if the character doesn't match, we stop immediately. 
        for word in range(1, len(strs)):
            if index_first_word == len(strs[word]) or strs[word][index_first_word] != char:
                return reference[:index_first_word]


string_list = ["flower","flow","flight"]
print(longestCommonPrefix(string_list))

# Vertical scanning
# No matter the language, the mental model is always a simple grid:
# 1. Take the first word as your baseline target.
# 2. Loop through each character position (column index col) of that first word.
# 3. Check the same column index across every other word (row index row).
# 4. Stop immediately if the row runs out of letters OR the letters don't match.

