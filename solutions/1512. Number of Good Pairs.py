class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        nums = nums[::-1]
        while nums:
            n = nums.pop()
            if n in nums:
                res += nums.count(n)
        return res
