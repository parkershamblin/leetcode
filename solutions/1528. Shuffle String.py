class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i in range(len(res)):
            res[indices[i]] = s[i]
        return ''.join(c for c in res)
