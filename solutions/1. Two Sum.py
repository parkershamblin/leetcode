class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, n in enumerate(nums):
            if target - n in lookup:
                return [i, lookup[target - n]]
            else:
                lookup[n] = i
​
