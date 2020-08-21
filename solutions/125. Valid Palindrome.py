class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.lower()
        res = ''.join([c for c in res if c.isdigit() or c.isalpha()])
        return res[::-1] == res
