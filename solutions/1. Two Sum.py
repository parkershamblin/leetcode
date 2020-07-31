class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while nums:
            n = nums.pop()
            if target - n in nums:
                return [len(nums), nums.index(target-n)]
