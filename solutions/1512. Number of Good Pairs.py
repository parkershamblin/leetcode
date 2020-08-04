class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # n*(n+1)/2
        # the sum of a list of positive consectuive numbers up to n is equal to average of the number elem??** forget
        """cant do this way. forget logic
        import collections
        collections.Counter(nums)
        """
        d = {}
        res = 0
        for i, n in enumerate(nums):
            if n in d:
                res += d[n]
                d[n] += 1
            else:
                d[n] = 1
        return res
