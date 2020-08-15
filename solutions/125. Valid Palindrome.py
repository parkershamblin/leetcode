class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalpha() or c.isdigit()]).lower()
        return s[::-1] == s
