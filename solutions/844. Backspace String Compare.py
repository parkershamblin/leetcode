class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_stack = []
        T_stack = []
        
        for i in S:
            if not S_stack:
                if i == "#":
                    pass
                else:
                    S_stack.append(i)
            else:
                if i == "#":
                    S_stack.pop()
                else:
                    S_stack.append(i)
        
        for i in T:
            if not T_stack:
                if i == "#":
                    pass
                else:
                    T_stack.append(i)
            else:
                if i == "#":
                    T_stack.pop()
                else:
                    T_stack.append(i)
        
        return S_stack == T_stack