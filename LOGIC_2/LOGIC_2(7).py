def make_chocolate(small, big, goal):
    kilos = goal / 5
    if big >= kilos:
        if small >= (goal - kilos * 5):
            return goal - kilos * 5
    if big < kilos:
        if small >= (goal - big * 5):
            return goal - big * 5
    return -1


print(make_chocolate(4, 1, 9))
