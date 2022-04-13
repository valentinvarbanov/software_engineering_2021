import re
from nltk.corpus import words

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
    word = re.sub(r'[^\w]', ' ', word.lower()).strip()
    english_vocab = set(w.lower() for w in words.words())
    for sub_words in word.split(' '):
        if sub_words not in english_vocab:
            return False

    return True
    
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
        decrypted_count = 0
        for word in input_words:
            decrypted_word = decrypt_word(word, key)
            result_words.append(decrypted_word)
            if check_word_valid(decrypted_word):
                decrypted_count += 1
                
        if decrypted_count >= len(input_words)/2:
            print(concat_result(result_words))
            print("key: " + str(key))
            return

decrypt()