class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for i, n in enumerate(numbers):
            if target - n in lookup:
                return [lookup[target - n] + 1, i + 1]
            else:
                lookup[n] = i
​
