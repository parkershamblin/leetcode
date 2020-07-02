class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                counter += 1
        return counter