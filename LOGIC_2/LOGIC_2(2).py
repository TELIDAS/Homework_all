def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if b == c:
        return a
    if a == c:
        return b
    if a == b:
        return c
    return a + b + c


print(lone_sum(1, 2, 3))
