class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = totMax = nums[0]
        for i in range(1, len(nums)):
            curMax = max(curMax+nums[i], nums[i])
            totMax = max(curMax, totMax)
        return totMax
​
