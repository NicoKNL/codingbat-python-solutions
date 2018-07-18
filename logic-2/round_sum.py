def round_sum(a, b, c):
    sum = 0
    sum += round10(a)
    sum += round10(b)
    sum += round10(c)
    return sum


def round10(num):
    remainder = num % 10
    if remainder < 5:
        return num - remainder
    else:
        return num - remainder + 10
