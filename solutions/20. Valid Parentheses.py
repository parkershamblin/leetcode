class Solution:
    def isValid(self, s: str) -> bool:
        # this was my own solution
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif stack:
                if stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True