from nltk.corpus import words
import re

def validate_word(word):
    word = re.sub(r'[^\w]', '', word.lower())
    english_vocab = set(w.lower() for w in words.words())
    if word in english_vocab:
        return True
    else:
        return False

def decrypt_a_single_word(word, key):
    decrypted_word = ''
    for letter in word:
        decrypted_letter = ''
        char_ord = ord(letter)
        if not ((ord('a') <= char_ord <= ord('z')) or (ord('A') <= char_ord <= ord('Z'))):
            decrypted_letter = letter
        elif ord(letter.lower()) - key < ord('a'):
            decrypted_letter = chr(char_ord + 26 - key)
        else:
            decrypted_letter = chr(char_ord - key)
        decrypted_word += decrypted_letter
    return decrypted_word

def print_res(words, key):
    res = ''
    for w in words:
        res = res + w + ' '
    print(res[:-1])
    print("key: " + key)

def decrypt(message):
    text = message.split(' ')
    words_count = len(text)

    for key in range(26):
        res_words = []
        for word in text:
            word_decrypted = decrypt_a_single_word(word, key)
            if validate_word(word_decrypted):
                res_words.append(word_decrypted)

        if len(res_words) == len(text):
            print_res(res_words, str(key))
            return

        elif len(res_words) > (0.5 * words_count):

            res_words = []
            for word in text:
                word_decrypted = decrypt_a_single_word(word, key)
                res_words.append(word_decrypted)
            print_res(res_words, str(key))
            return
 
message = input()
decrypt(message)