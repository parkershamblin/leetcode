class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        for c in s:
            a ^= ord(c)
        for c in t:
            a ^= ord(c)
        return chr(a)
