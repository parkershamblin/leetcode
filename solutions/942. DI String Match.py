# redo. Try to come up with a solution that does not requie a try/except clause
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = []
        right, left = 0, len(S)
        for i in range(len(S)+1):
            try:
                if S[i] == "I":
                    res.append(right)
                    right += 1
                else:
                    res.append(left)
                    left -= 1
            except IndexError as e:
                res.append(right)
                right += 1
        return res