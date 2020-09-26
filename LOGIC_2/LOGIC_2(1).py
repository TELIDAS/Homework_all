def make_bricks(small, big, goal):
    return goal % 5 >= 0 and goal % 5 - small <= 0 and small + 5 * big >= goal


print(make_bricks(3, 1, 8))
