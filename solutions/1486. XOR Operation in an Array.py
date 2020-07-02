class Solution:
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [(start + 2*i) for i in range(0, n)]
        xor_res = nums[0]
        for i in range(1, n):
            xor_res = xor_res^nums[i]
        return xor_res