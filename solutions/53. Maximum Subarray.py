class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = totalMax = nums[0]
        for i in range(1, len(nums)):
            curMax = max(curMax+nums[i], nums[i])
            totalMax = max(curMax, totalMax)
        return totalMax
