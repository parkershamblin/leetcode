class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = [n for n in A if n % 2 == 0]
        odd = [n for n in A if n % 2 != 0]
        res = []
        while even and odd:
            res.append(even.pop())
            res.append(odd.pop())
        res.extend(even if even else odd)
        return res
