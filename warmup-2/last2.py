def last2(str):
  count = 0
  if not len(str) or len(str) == 1:
    return count
  for i in range(len(str) - 1):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count - 1
