def make_bricks(small, big, goal):
  n_big = math.floor(goal / 5)
  goal -= min([big, n_big]) * 5

  return small >= goal
