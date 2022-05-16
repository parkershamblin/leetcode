class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Brute Force
        answer = -1
        n = len(nums)
        for i in range(0, n):
            for j in range(1, n):
                if (i != j) and (nums[i] + nums[j] <  k):
                    answer = max(answer, nums[i] + nums[j])
        return answer
​
