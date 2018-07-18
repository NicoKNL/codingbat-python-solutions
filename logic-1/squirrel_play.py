def squirrel_play(temp, is_summer):
  min_temp = 60
  max_temp = 90

  if is_summer:
    max_temp = 100

  return min_temp <= temp <= max_temp
