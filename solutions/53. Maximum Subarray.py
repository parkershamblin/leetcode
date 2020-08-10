class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = total_max = nums[0]
        for n in nums[1:]:
            cur_max = max(cur_max + n, n)
            total_max = max(total_max, cur_max)
        return total_max
