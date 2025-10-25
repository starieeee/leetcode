def pivotIndex(nums):
    tol = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = tol - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1