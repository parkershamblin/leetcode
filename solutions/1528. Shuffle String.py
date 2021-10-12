class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['' for i in range(0, len(s))]
        for i in range(0, len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)
