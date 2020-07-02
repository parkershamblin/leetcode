class Solution:
    def isPalindrome(self, x: int) -> bool:
        # solution with converting int to string
        if x >= 0:
            res = int(str(x)[::-1])
            if res == x:
                return True
        else:
            return False