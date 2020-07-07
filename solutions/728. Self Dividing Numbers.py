class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if all([int(j) != 0 and i % int(j) == 0 for j in str(i)]):
                res.append(i)
        return res