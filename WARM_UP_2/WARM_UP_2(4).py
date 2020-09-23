string = input("wordino: ")
resultino = " "
for m in range(0, len(string)):
    resultino = resultino + string[:m +1]
print(resultino)
