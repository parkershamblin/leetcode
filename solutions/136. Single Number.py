class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Approach 1: bit manipulation
        a = 0
        for n in nums:
            a ^= n
        return a
​
​
        # Approach 2:  Math
        return 2 * sum(set(nums)) - sum(nums)
​
​
        # Approach 3: hash table
        c = collections.Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k
