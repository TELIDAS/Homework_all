# string_bits
string = input(": ")
result = ""
for n in range(0, len(string)):
    if n % 2 == 0:
        result += string[n]
print(result)