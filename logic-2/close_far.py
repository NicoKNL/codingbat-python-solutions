def close_far(a, b, c):
  a_b = abs(a-b)
  a_c = abs(a-c)
  b_c = abs(b-c)
  return (a_b<=1 and a_c>=2 and b_c>=2) or (a_c<=1 and a_b>=2 and b_c>=2)
