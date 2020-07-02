class Solution:
    def freqAlphabets(self, s: str) -> str:
        import string
        letters = list(string.ascii_lowercase)
        nums = [str(n) for n in range(1, 10)]
        nums.extend([str(n) for n in range(10, 27)])
        d = dict(zip(nums, letters))
        
        output = ""
        
        for i in range(len(s)):
            if len(s[i:]) == 1 and s[i] != "#":
                output += d[f'{s[i]}']
            try:
                if s[i] != "#" and s[i+1] != "#":
                    try:
                        if s[i+2] != "#":
                            output += d[f'{s[i]}']
                    except IndexError:
                        output += d[f'{s[i]}']
                if s[i+2] == "#":
                    output += d[f'{s[i]}{s[i+1]}']
            except IndexError:
                pass
                
        return output
                