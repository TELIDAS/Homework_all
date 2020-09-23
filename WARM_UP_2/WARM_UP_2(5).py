string = input("")
count = 0
for a in range(len(string)-2):
    if string[a:a+2] == string[-2:]:
        count += 1
print(count)
