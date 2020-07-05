class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i, v in enumerate(arr2):
            d[v] = i
        
        res = []
        for i in arr2:
            res += [i] * arr1.count(i)
        for i in sorted(list(set(arr1) - set(arr2))):
            res += [i] * arr1.count(i)
        return res