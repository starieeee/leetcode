class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracketMap = {'[':']', '{':'}', '(':')'}
        for char in s:
            if char in bracketMap:
                stack.append(char)
            elif stack and bracketMap[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack