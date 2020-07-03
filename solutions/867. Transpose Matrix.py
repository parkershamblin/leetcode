class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(A[0])
        for i in range(n):
            res.append([row[i] for row in A])
        return res