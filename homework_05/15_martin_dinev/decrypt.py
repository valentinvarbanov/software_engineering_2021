from posixpath import split
from nltk.corpus import wordnet

key = 0
str = input()

for i in range(0, -25, -1):
    for word in str.split():
        correctWord = ""
        for char in word:
            if (64 < ord(char) < 91 or 96 < ord(char) < 123):
                correctWord += chr(ord(char) + i)
        if not wordnet.synsets(correctWord):
            break
        else:
            if word == str.split()[len(str.split())-1]:
                key = -i

newStr = ""
for word in str.split():
    correctWord = ""
    for char in word:
        if (64 < ord(char) < 91 or 96 < ord(char) < 123):
            correctWord += chr(ord(char) - key)
        else:
            correctWord += char
    if not word == str.split()[len(str.split())-1]:
        newStr += correctWord + " "
    else:
       newStr += correctWord 

print(newStr)
print("key:", key)