class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        while nums.count(0) > 0:
            nums.remove(0)
            counter += 1
        for i in range(counter):
            nums.append(0)