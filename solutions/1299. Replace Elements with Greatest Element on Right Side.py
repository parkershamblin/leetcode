class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(arr):
            try:
                res.append(max(arr[i+1:]))
            except (IndexError, ValueError) as e:
                res.append(-1)
        return res