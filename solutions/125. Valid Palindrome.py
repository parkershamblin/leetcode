class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.lower()
        res = ''.join([c for c in res if c.isalnum()])
        return res[::-1] == res
