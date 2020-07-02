class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        for i in range(0, len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res