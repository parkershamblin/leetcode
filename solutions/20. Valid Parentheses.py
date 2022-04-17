class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False
        stack = []
        dic = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in (")", "]", "}"):
                if not stack or stack.pop() != dic[i]:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
