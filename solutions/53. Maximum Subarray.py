class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = tot_max = nums[0]
        for n in nums[1:]:
            cur_max = max(cur_max+n, n)
            tot_max = max(cur_max, tot_max)
        return tot_max
