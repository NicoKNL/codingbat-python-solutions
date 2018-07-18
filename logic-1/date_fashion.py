def date_fashion(you, date):
  result = 0

  if you >= 8 or date >= 8:
    result += 1

  if you <= 2 or date <= 2:
    return 0

  if you >= 2 or date >= 2:
    result += 1

  return result
