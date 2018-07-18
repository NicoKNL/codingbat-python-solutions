def lone_sum(a, b, c):
  sum = 0
  values = [a, b, c]
  for each in values:
    if values.count(each) == 1:
      sum += each

  return sum
