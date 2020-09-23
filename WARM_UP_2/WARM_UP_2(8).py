# array 123
number = [1, 1, 2, 3, 1]
bool1 = False
bool2 = False
bool3 = False

for t in range(len(number)):
    if number[t] == 1:
        bool1 = True
    if number[t] == 2:
        bool2 = True
    if number[t] == 3:
        bool3 = True
if bool1 == True and bool2 == True and bool3 == True:
    print(True)
else:
    print(False)
