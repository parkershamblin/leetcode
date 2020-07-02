class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            try:
                return haystack.find(needle)
            except Exception as e:
                return 0
        else:
            return 0