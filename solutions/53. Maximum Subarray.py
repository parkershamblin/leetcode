class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = totMax = nums[0]
        for num in nums[1:]:
            curMax = max(curMax+num, num)
            totMax = max(curMax, totMax)
        return totMax
​
