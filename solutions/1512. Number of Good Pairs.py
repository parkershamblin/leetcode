class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum((n*(n-1)//2) for n in collections.Counter(nums).values())
​
