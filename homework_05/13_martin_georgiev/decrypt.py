from nltk.corpus import wordnet

encrypted_string = input()

int_a = ord('a')
int_z = ord('z')
int_A = ord('A')
int_Z = ord('Z')
difference = int_Z - int_A + 1

def decrypt(encrypted_string):
    key = 0
    for i in range(0, 25):
        counter = 0
        for word in encrypted_string.split():
            correct_word = ""
            for char in word:
                symbol_integer = ord(char)
                result = symbol_integer

                if int_A <= symbol_integer <= int_Z:
                    result -= i
                    if not (int_A <= result <= int_Z):
                        result += difference
                    correct_word += chr(result)
                elif int_a <= symbol_integer <= int_z:
                    result -= i
                    if not (int_a <= result <= int_z):
                        result += difference
                    correct_word += chr(result)
                else:
                    correct_word += ''
            if wordnet.synsets(correct_word):
                counter += 1
        if counter > (50/100)*len(encrypted_string.split()):
            key = i
            break
    return key


def apply_key(key):
    decryptedString = ""
    for char in encrypted_string:
        symbol_integer = ord(char)
        result = symbol_integer

        if int_A <= symbol_integer <= int_Z:
            result -= key
            if not (int_A <= result <= int_Z):
                result += difference
        if int_a <= symbol_integer <= int_z:
            result -= key
            if not (int_a <= result <= int_z):
                result += difference
        decryptedString += chr(result)
    return decryptedString

key = decrypt(encrypted_string)
print(apply_key(key))
print("key:", key)
