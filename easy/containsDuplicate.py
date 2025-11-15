class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = len(nums)
        set2 = len(set(nums))
        return True if set1 != set2 else False