class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in lookup.values():
                stack.append(char)
            if char in lookup.keys():
                if not stack or stack.pop() != lookup[char]:
                    return False
        if len(stack) == 0:
            return True
