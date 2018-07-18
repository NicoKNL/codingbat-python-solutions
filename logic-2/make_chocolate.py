def make_chocolate(small, big, goal):
    n_big = int(math.floor(goal / 5))
    goal -= min([big, n_big]) * 5

    if small >= goal:
        return goal
    else:
        return -1
