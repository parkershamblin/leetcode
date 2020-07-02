class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        uniq = set()
        for a in A:
            if a not in uniq:
                uniq.add(a)
            else:
                return a