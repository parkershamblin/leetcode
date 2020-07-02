class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i > target[-1]:
                break
            elif i in target:
                res.append("Push")
            else:
                res += ["Push", "Pop"]
        return res