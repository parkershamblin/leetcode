class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        res = ""
        for c in s.lower():
            if c in (string.ascii_lowercase + string.digits):
                res += c
        return res == res[::-1]
        
