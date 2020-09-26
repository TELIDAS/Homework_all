def close_far(a, b, c):
    condition1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
    condition2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
    return condition1 or condition2


print(close_far(4, 1, 3))
