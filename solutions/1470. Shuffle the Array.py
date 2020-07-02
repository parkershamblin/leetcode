class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        start_1 = 0
        start_2 = n
        xs = [x for x in nums[start_1:start_2]]
        ys = [y for y in nums[start_2:]]
        result = []
        for i in range(0, len(xs)):
            result.append(xs[i])
            result.append(ys[i])
        return result