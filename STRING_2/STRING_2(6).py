def xyz_there(string):
    for i in range(len(string)):
        if string[i] != "." and string[0:-1] == "xyz":
            return True
        if string[0:3] == "xyz":
            return True
        return False

print(xyz_there("abc.xyz"))
print(xyz_there("xyz.abc"))
