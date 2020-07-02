class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = []
        for i in range(100):
            for j in range(100):
                n = x**i + y**j
                if n <= bound:
                    ans.append(n)
        return sorted(set(ans))