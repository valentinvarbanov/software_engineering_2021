from nltk.corpus import words as nltk_words

def CheckWord(word):
    dictionary = dict.fromkeys(nltk_words.words(), True)
    try:
        x = dictionary[word]
        return True
    except KeyError:
        return False

def Decryption(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - key - 64) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - key - 96) % 26 + 97)
        else:
            decrypted_message += char

        if not CheckWord(decrypted_message):
            break

    return decrypted_message