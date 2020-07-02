class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [sum(nums[:i+1]) for i in range(len(nums))]
        return running_sum