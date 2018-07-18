def count_hi(str):
  count = 0
  if len(str) < 2:
    return count

  else:
    for i in range(len(str)-1):
      if str[i:i+2] == "hi":
        count += 1

  return count
