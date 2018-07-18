def lucky_sum(a, b, c):
  sum = 0
  skip = False
  values = [a, b, c]
  for v in values:
    if v == 13:
      break
    else:
      sum += v
  return sum
