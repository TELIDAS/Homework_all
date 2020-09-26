def making_centre(tag, string):
    return tag[:2]+string+tag[2:5]


print(making_centre("<<>>", "WOOHOO"))
print(making_centre("<<>>", "YAY"))