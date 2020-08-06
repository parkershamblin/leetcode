class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, n in enumerate(nums):
            if (target - n) in lookup:
                return [lookup[(target - n)], i]
            else:
                lookup[n] = i
​
