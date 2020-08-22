class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # gauss' formula math approach
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
​
    def missingNumber1(self, nums: List[int]) -> int:
        # bit manipulation approach
        a = 0
        for i in range(len(nums) + 1):
            a ^= i
        for n in nums:
            a ^= n
        return a
​
