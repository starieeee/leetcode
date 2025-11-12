class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""
        for char in s.lower():
            if char.isalnum():
                res += char
        return res == res[::-1]