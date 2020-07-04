class Solution:
    def sumZero(self, n: int) -> List[int]:
        target = 0
        res = []
        for i in range(n-1):
            res.append(i)
        dif = target - sum(res)
        res.append(dif)
        return res