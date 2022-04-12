from posixpath import split
from nltk.corpus import wordnet

key = 0
str = input()

for i in range(0, -25, -1):
    for word in str.split():
        correct_word = ""
        for char in word:
            if (64 < ord(char) < 91 or 96 < ord(char) < 123):
                correct_word += chr(ord(char) + i)
        if not wordnet.synsets(correct_word):
            break
        else:
            if word == str.split()[len(str.split())-1]:
                key = -i

new_str = ""
for word in str.split():
    correct_word = ""
    for char in word:
        if (64 < ord(char) < 91 or 96 < ord(char) < 123):
            correct_word += chr(ord(char) - key)
        else:
            correct_word += char
    if not word == str.split()[len(str.split())-1]:
        new_str += correct_word + " "
    else:
       new_str += correct_word 

print(new_str)
print(key)
