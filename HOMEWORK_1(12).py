text = input("")
if len(text) < 3:
    print(text * 3)
else:
    new_text = text[0:3]
    print(new_text*3)
print(input()[:3]*3)
