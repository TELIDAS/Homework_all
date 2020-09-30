def count_code(string):
    result = 0
    for i in range(0, len(string)-3):
        if string[i:i+2] == "co" and string[i+3] == "e":
            result += 1
        return result

print(count_code("codexxcode"))
print(count_code("aaacodebbb"))
print(count_code("cozexxcope"))
