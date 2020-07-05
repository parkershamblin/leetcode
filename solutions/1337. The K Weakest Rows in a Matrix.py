class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowSums = []
        for i, row in enumerate(mat):
            rowSums.append((sum(row), i))
        rowSums = sorted(rowSums)
        res = [i[1] for i in rowSums[:k]]
        return res