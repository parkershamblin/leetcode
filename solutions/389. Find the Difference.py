class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        for character in s:
            a ^= ord(character)
        for character in t:
            a ^= ord(character)
        return chr(a)
