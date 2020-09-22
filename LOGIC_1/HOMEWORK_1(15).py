temperature = int(input(""))
summer = input("")
if temperature in range(60, 101) and summer == "True":
    print("True")
elif temperature in range(60, 91) and summer == "False":
    print("True")
else:
    print("False")
