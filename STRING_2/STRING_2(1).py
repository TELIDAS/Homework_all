def double_char(string):
    result = ''
    for i in string:
        result += i * 2
    return result

print(double_char(("The")))
print(double_char("AAbb"))
print(double_char("Hi-There"))
