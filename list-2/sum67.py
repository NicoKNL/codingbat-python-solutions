def sum67(nums):
    sum = 0
    locked = False
    for num in nums:
        if num == 6:
            locked = True
            continue
        elif num == 7 and locked:
            locked = False
            continue

        if not locked:
            sum += num

    return sum
