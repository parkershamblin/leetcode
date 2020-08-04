class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k
