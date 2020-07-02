class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if "IV" in s:
            res += 4
            s = s.replace("IV", "")
        if "IX" in s:
            res += 9
            s = s.replace("IX", "")
        if "XL" in s:
            res += 40
            s = s.replace("XL", "")
        if "XC" in s:
            res += 90
            s = s.replace("XC", "")
        if "CD" in s:
            res += 400
            s = s.replace("CD", "")
        if "CM" in s:
            res += 900
            s = s.replace("CM", "")
        res += s.count("I")
        res += s.count("V") * 5
        res += s.count("X") * 10
        res += s.count("L") * 50
        res += s.count("C") * 100
        res += s.count("D") * 500
        res += s.count("M") * 1000
        return res