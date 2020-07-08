class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if 1 <= len(nums) <= 2:
            if nums[0] == target:
                return 0
            elif nums[-1] == target:
                return 1
            
        left, mid, right = 0, len(nums) // 2, len(nums)-1
        while left < mid < right:
            print(right)
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] > target:
                right = mid
                mid = (left + right) // 2
            elif nums[mid] < target:
                left = mid
                mid = (left + right) // 2
        return -1