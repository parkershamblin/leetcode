class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {')': '(', '}':'{', ']': '['}
        stack = []
        for c in s:
            if c in hash_table.keys():
                if not stack or stack.pop() != hash_table[c]:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
