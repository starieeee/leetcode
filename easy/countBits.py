class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, n + 1):
            result.append(result[i // 2] + i%2)
        return result
        