vacation = input("")
day = int(input(""))
if vacation == "not vacation":
    if 1 <= day <= 5:
        print("7:00")
    if day == 0 or day == 6:
        print("10:00")
elif vacation == "vacation":
    if 1 <= day <= 5:
        print("10:00")
    if day == 0 or day == 6:
        print("off")
else:
    print("off")
