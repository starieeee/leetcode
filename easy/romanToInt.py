class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sSplit = s.split()
        tol = 0
        for i in range(len(s)):
            if s[i] == "I":
                val = 1
            elif s[i] == "V":
                val = 5
            elif s[i] == "X":
                val = 10
            elif s[i] == "L":
                val = 50
            elif s[i] == "C":
                val = 100
            elif s[i] == "D":
                val = 500
            elif s[i] == "M":
                val = 1000
            
            if i + 1 < len(s):
                if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                    tol -= val
                    continue
                if s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                    tol -= val
                    continue
                if s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                    tol -= val
                    
            tol += val
        return tol