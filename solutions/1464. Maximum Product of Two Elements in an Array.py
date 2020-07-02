class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = max(nums)
        nums.remove(max_1)
        max_2 = max(nums)
        return (max_1-1)*(max_2-1)