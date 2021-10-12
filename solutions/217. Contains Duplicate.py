class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):  # duplicate exist
            return True
        else:
            return False
