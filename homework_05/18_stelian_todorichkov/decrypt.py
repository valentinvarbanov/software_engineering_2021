from nltk.corpus import words
import re

UPPERCASE_A = ord('A')
UPPERCASE_Z = ord('Z')
LOWERCASE_A = ord('a')
LOWERCASE_Z = ord('z')

def decrypt_word(encrypt_word, key):
    decrypted_word = ""

    for letter in encrypt_word:
        decrypt_letter = ''
        letter_ord = ord(letter)
        if not ((LOWERCASE_A <= letter_ord <= LOWERCASE_Z) or (UPPERCASE_A <= letter_ord <= UPPERCASE_Z)):
            decrypt_letter = letter
        elif ord(letter.lower()) - key < LOWERCASE_A:
            decrypt_letter = chr(letter_ord + 26 - key)
        else:
            decrypt_letter = chr(letter_ord - key)
        decrypted_word += decrypt_letter

    return decrypted_word

def check_word_valid(word):
    word = re.sub(r'[^\w]', '', word.lower())
    english_vocab = set(w.lower() for w in words.words())
    if word in english_vocab:
        return True
    else:
        return False

def concat_result(result_words):
    result = ""
    
    for word in result_words:
        result = result + word + " "
    
    return result.strip()

def decrypt():
    input_str = input()
    input_words = input_str.split(' ')

    for key in range(26):
        result_words = []
        for word in input_words:
            decrypted_word = decrypt_word(word, key)
            if check_word_valid(decrypted_word):
                result_words.append(decrypted_word)
            else:
                break
        if len(result_words) == len(input_words):
            print(concat_result(result_words))
            print(key)
            return

decrypt()
