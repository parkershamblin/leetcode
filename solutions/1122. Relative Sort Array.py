class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i, v in enumerate(arr2):
            d[v] = i
        
        res = []
        for i in arr2:
            res += [i] * arr1.count(i)
        res = res + sorted(i for i in arr1 if i not in arr2)
        return res