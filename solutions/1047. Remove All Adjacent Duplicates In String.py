class Solution:
    def removeDuplicates(self, S: str) -> str:
        for i in S:
            if i+i in S:
                S = S.replace(i+i, "")
        return S