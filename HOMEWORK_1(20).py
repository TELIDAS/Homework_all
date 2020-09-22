a = input("")
n = int(input(""))
if n in range(1, 11):
    print("True")
elif n not in range(1, 11) and a == "True":
    print("True")
else:
    print("False")
