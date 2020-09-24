# array front9
nine = []
for i in range(5):
    nine.append(input()))
if len(nine) < 4:
    if 9 in nine:
        print(True)
first_4 = nine[:4]

if 9 in first_4:
    print(True)
else:
    print(False)
