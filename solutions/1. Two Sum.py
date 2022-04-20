class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            diff = target - num
            for j, num2 in enumerate(nums[i+1:]):
                if num2 == diff:
                    return [i, j+i+1]
                    
