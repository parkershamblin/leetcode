class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        stack = []
        
        for char in s:
            stack.append(char)
            if stack.count("L") == stack.count("R"):
                counter += 1
        
        return counter