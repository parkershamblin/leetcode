class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(", "}":"{", "]":"["}
        
        for char in s:
            if char in lookup.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != lookup[char]:
                    return False
​
        return len(stack) == 0
