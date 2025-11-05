class Solution(object):
    from collections import Counter
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        length = 0
        hasOdd = False

        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                hasOdd = True
        if hasOdd:
            length += 1
        return length
