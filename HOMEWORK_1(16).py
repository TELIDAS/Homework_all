day = input("")
speed = int(input(""))
if day == "birthday":
    speed = speed + 5
if speed in range(0, 60):
    print(0)
if speed in range(61, 80):
    print(1)
if speed in range(81, 1000):
    print(2)
