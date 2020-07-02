# REDO try to create solution with no try/except clauses
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)