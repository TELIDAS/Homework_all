def first(string):
    if len(string)<= 2:
        return string
    else:
        return string[:2]



print(first("hello"))
print(first("abcdefg"))
print(first("ab"))