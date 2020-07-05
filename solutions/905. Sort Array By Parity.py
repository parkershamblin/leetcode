class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        evens = []
        for i in A:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        res = evens + odds
        return res