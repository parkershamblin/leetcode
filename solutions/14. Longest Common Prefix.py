class Solution:
    def longestCommonPrefix(self, strs):
        if strs:
            # sort list by length of elements
            strs = sorted(strs, key=len)
            res = ""
            for i, char in enumerate(strs[0]):
                if all([word[i] == char for word in strs[1:]]):
                    res += char
                else:
                    break  # break if next character in prefix is not found
            return res
        else:
            return ""