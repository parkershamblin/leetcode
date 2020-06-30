```````````#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError as e:
            for i in nums:
                if i > target:
                    return nums.index(i)
            return len(nums) # item should be placed at end of list
# @lc code=end

