class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        #SECOND SOLUTION
        n = len(nums)
        total = (n + 1) // 2 * n
        return total - sum(nums)


