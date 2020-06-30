#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solution with converting int to string
        if x >= 0:
            res = int(str(x)[::-1])
            if res == x:
                return True
        else:
            return False
# @lc code=end

