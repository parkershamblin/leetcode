class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, char in enumerate(s):
            res[indices[i]] = char
        return ''.join(char for char in res)
