class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = []
        cur = 0
        end = len(S)
        for i in range(len(S)+1):
            try:
                if S[i] == "I":
                    res.append(cur)
                    cur += 1
                else:
                    res.append(end)
                    end -= 1
            except IndexError as e:
                res.append(cur)
                cur += 1
        return res