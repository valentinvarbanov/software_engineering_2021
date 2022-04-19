from nltk.corpus import wordnet

key = 0
str = input()

A_INTEGER = ord('A')
Z_INTEGER = ord('Z')

a_INTEGER = ord('a')
z_INTEGER = ord('z')

difference = (Z_INTEGER - A_INTEGER) + 1

for i in range(0, -25, -1):
    counter = 0
    for word in str.split():
        correctWord = ""
        for char in word:
            symbol_integer = ord(char)
            result = symbol_integer

            if A_INTEGER <= symbol_integer <= Z_INTEGER:
                result += i
                if not (A_INTEGER <= result <= Z_INTEGER):
                    result += difference
            elif a_INTEGER <= symbol_integer <= z_INTEGER:
                result += i
                if not (a_INTEGER <= result <= z_INTEGER):
                    result += difference
            correctWord += chr(result)
        if wordnet.synsets(correctWord):
            counter += 1
    if counter > (60/100)*len(str.split()):
        key = -i
        break

newStr = ""
for symbol in str:
    symbol_integer = ord(symbol)
    result = symbol_integer

    if A_INTEGER <= symbol_integer <= Z_INTEGER:
        result -= key
        if not (A_INTEGER <= result <= Z_INTEGER):
            result += difference
    elif a_INTEGER <= symbol_integer <= z_INTEGER:
        result -= key
        if not (a_INTEGER <= result <= z_INTEGER):
            result += difference
    newStr += chr(result)

print(newStr)
print("key:", key)