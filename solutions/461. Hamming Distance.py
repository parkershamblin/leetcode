class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return str(bin(x ^ y)).count("1")