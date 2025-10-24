def twoSum(nums, target):
    checked = {}
    for i in range(len(nums)):
        num = nums[i]
        completed = target - num
        if completed in checked:
            return [checked[completed], i]
        checked[num] = i
print(twoSum([2,7,11,15], 9))