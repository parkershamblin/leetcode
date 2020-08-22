# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, lower=0, upper=len(nums))
    
    def helper(self, nums, lower, upper):
        if lower < upper:
            mid = (lower + upper) // 2
            root = TreeNode(val=nums[mid])
            root.left = self.helper(nums, lower=lower, upper=mid)
            root.right = self.helper(nums, lower=mid+1, upper=upper)
            return root
