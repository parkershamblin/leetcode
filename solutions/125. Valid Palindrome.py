class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(c for c in s.lower() if c.isalnum())
        return res == res[::-1]
        
