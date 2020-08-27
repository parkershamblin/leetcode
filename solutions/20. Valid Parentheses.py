class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in lookup.keys():
                if not stack or stack.pop() != lookup[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
