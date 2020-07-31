class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = nums
        while stack:
            n = stack.pop()
            if target - n in stack:
                return [len(stack), stack.index(target-n)]
