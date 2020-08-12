class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        hash_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for i, c in enumerate(s):
            if i > 0:
                if c == "V" and s[i-1] == "I":
                    res -= 2 * hash_table[s[i-1]]
                if c == "X" and s[i-1] == "I":
                    res -= 2 * hash_table[s[i-1]]
                if c == "L" and s[i-1] == "X":
                    res -= 2 * hash_table[s[i-1]]
                if c == "C" and s[i-1] == "X":
                    res -= 2 * hash_table[s[i-1]]
                if c == "D" and s[i-1] == "C":
                    res -= 2 * hash_table[s[i-1]]
                if c == "M" and s[i-1] == "C":
                    res -= 2 * hash_table[s[i-1]]
            res += hash_table[c]
        
        return res
