class Solution(object):
    # define a function to reverse bits of a 32-bit unsigned integer
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        reverse_n = 0
        for _ in range(32):
            reverse_n = reverse_n << 1
            bit = n & 1
            reverse_n = reverse_n | bit
            n = n >> 1
        return reverse_n