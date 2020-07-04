class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = []
        evens = []
        odds = []

        for i in A:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        for i in range(len(odds)):
            res.extend([evens[i], odds[i]])

        return res