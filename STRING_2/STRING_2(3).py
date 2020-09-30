def cat_dog(string):
    a = string.split("cat")
    b = string.split("dog")
    if len(a) == len(b):
        return True
    else:
        return False


print(cat_dog("catdog"))
print(cat_dog("catcat"))
print(cat_dog("1cat1cadodog"))
