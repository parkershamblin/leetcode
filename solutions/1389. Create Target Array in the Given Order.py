class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []  # initally target array is empty
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target