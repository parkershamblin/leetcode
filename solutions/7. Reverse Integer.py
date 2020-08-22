class Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)
        number = int(str(sign * x)[::-1])
        return sign * number if number < pow(2, 31) else 0
