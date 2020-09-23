# string match
a = input(": ")
b = input(":")
min_len = min(len(a), len(b))
count = 0
for w in range(min_len -1):
    if a[w:w+2] == b[w:w+2]:
        count += 1
print(count)
