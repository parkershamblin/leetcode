#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
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

# @lc code=end

