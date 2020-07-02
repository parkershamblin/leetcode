class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dif = target - nums[i]
            nums2 = [j for j in nums]
            nums2[i] = "#"
            if dif in nums2:
                return [i, nums2.index(dif)]