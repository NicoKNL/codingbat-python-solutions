def sum13(nums):
    sum = 0
    skip = False
    if not nums:
        return sum
    else:
        for num in nums:
            if num == 13:
                skip = True
                continue
            if skip:
                skip = False
                continue
            if not skip:
                sum += num

    return sum
