class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphabet = string.ascii_lowercase
        d = {c: 0 for c in alphabet}
        
        for k, v in d.items():
            d[k] = min([word.count(k) for word in A])  # Why doesn't return 0 for all values?

        res = []
        for c, n in d.items():
            if n > 0:
                res += [c] * n
        return res