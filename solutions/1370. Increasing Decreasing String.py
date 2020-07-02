class Solution:
    def sortString(self, s: str) -> str:
        alphabet_string = string.ascii_lowercase
        alphabet = list(alphabet_string)
        res = ""
        char_counts = []
        while len(s) > len(res):
            for char in alphabet:
                char_counts += [s.count(char)]
            for i in range(len(alphabet)):
                if char_counts[i] > 0:
                    res += alphabet[i]
                    char_counts[i] -= 1
            for i in reversed(range(0, len(alphabet))):
                if char_counts[i] > 0:
                    res += alphabet[i]
                    char_counts[i] -= 1
        return res