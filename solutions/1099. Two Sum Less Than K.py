class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # sorted O(n*log(n))
        nums = sorted(nums)
        answer = -1
        left, right = 0, (len(nums) - 1)
        while left < right:
            my_sum = nums[left] + nums[right]
            if (my_sum < k):
                answer = max(answer, my_sum)
                left += 1
            else:
                right -= 1
        return answer
​
