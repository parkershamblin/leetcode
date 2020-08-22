class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = n * (n + 1) // 2
        return tmp - sum(nums)
