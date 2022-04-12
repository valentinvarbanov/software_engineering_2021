from nltk.corpus import wordnet, words
from nltk.tokenize import RegexpTokenizer
from nltk import WordNetLemmatizer
import re

UPPERCASE_A = ord('A')
UPPERCASE_Z = ord('Z')
LOWERCASE_A = ord('a')
LOWERCASE_Z = ord('z')

def decrypt_word(encrypt_word, key):
    decrypted_word = ""

    for letter in encrypt_word:
        decrypted_letter = ''
        letter_code = ord(letter)
        if not ((LOWERCASE_A <= letter_code <= LOWERCASE_Z) or (UPPERCASE_A <= letter_code <= UPPERCASE_Z)):
            decrypted_letter = letter
        elif ord(letter.lower()) - key < LOWERCASE_A:
            decrypted_letter = chr(letter_code + 26 - key)
        else:
            decrypted_letter = chr(letter_code - key)
        decrypted_word += decrypted_letter

    return decrypted_word

def check_is_word_valid(word):
    tokenizer = RegexpTokenizer(r'\w+')
    lemma = WordNetLemmatizer()

    word_token = tokenizer.tokenize(word)[0]
    lemma_word = lemma.lemmatize(tokenizer.tokenize(word)[0])	

    if word_token.lower() in words.words() or wordnet.synsets(lemma_word):
        return True
    return False


def concat_result(result_words):
    result = ""

    for word in result_words:
        result = result + word + " "

    return result.strip()

def decrypt_text():
    input_text = input()
    input_words = input_text.split(' ')

    for key in range(26):
        result_words = []
        for word in input_words:
            decrypted_word = decrypt_word(word, key)
            if check_is_word_valid(decrypted_word):
                result_words.append(decrypted_word)
            else:
                break
        if len(result_words) == len(input_words):
            print(concat_result(result_words))
            print(key)
            return

decrypt_text()