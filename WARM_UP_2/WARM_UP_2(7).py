# array front9
nine = [1, 2, 3, 4, 9]
if len(nine) < 4:
    if 9 in nine:
        print(True)
first_4 = nine[:4]

if 9 in first_4:
    print(True)
else:
    print(False)