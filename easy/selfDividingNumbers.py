class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right + 1):
            isDigit = True

            for digitChar in str(i):
                digit = int(digitChar)

                if digit == 0 or i % digit  != 0:
                    isDigit = False
                    break
            
            if isDigit:
                result.append(i)
        return result
