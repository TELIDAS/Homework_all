# array count9
nine = [1, 9, 9]
for i in range(5):
    nine.append(int(input()))
count = 0
for a in nine:
    if a == 9:
        count += 1
print(count)
