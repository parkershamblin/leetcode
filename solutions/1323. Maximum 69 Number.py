class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        if '6' in num:
            i = num.find('6')
            res = num[:i]
            res += '9'
            if i != len(num):
                res += num[i+1:]
            else:
                pass
            return int(res)
        return int(num)