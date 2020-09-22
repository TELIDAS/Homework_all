z = int(input(""))
x = int(input(""))
negative = input("")
if (z < 0) and (x < 0) and negative == "True":
    print("True")
if z > 0 and x < 0 or z < 0 and x > 0 and negative == "False":
    print("True")
else:
    print("False")
