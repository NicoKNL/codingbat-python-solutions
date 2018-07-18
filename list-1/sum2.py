def sum2(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    else:
        return sum(nums[:2])
