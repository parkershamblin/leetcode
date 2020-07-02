class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i, row in enumerate(matrix):
            # print(row)
            for j, elem in enumerate(row):
                if elem == min(row) and elem == max([row[j] for row in matrix]):
                    res.append(elem)
        return res