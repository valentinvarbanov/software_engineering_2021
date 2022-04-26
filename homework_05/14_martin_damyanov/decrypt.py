from nltk.corpus import words
import re

def decrypt():
    input_str = input()
    input_words = input_str.split(' ')
    words_count = len(input_words)

    for key in range(26):
        result_words = []
        not_recognized = []
        old_result_words = len(result_words)
        for word in input_words:
            dec_word = decrypt_word(word, key)
            if is_valid(dec_word):
                result_words.append(dec_word)
            #else:
            #    result_words.append("err") #err for Error
            #    not_recognized.append(dec_word)

        if len(result_words) == len(input_words):
            print_result(result_words, str(key))
            return

        elif len(result_words) > (0.5 * words_count):

            result_words = []
            for word in input_words:
                dec_word = decrypt_word(word, key)
                result_words.append(dec_word)
            print_result(result_words, str(key))
            return
            
def print_result(result_words, key):
    result = ""
    for word in result_words:
        result = result + word + " "
    print(result[:-1])
    print("key: " + key)

def decrypt_word(enc_word, key):
    dec_word = ""
    for char in enc_word:
        dec_char = ''
        letter_ord = ord(char)
        if not ((ord('a') <= letter_ord <= ord('z')) or (ord('A') <= letter_ord <= ord('Z'))):
            dec_char = char
        elif ord(char.lower()) - key < ord('a'):
            dec_char = chr(letter_ord + 26 - key)
        else:
            dec_char = chr(letter_ord - key)
        dec_word += dec_char
    return dec_word

def is_valid(word):
    word = re.sub(r'[^\w]', '', word.lower())
    english_vocab = set(w.lower() for w in words.words())
    if word in english_vocab:
        return True
    else:
        return False

decrypt()