from nltk.corpus import wordnet, words
from nltk.tokenize import RegexpTokenizer
from nltk import WordNetLemmatizer

UPPERCASE_A = ord('A')
UPPERCASE_Z = ord('Z')
LOWERCASE_A = ord('a')
LOWERCASE_Z = ord('z')
ALPHABET_LENGTH = LOWERCASE_Z + 1 - LOWERCASE_A

def decrypt_text():
    encrypted_message = input()
    encrypted_words, decrypted_words = encrypted_message.split(' '), []

    right_key = 0
 
    for key in range(0, 26):
        for encrypted_word in encrypted_words:

            decrypted_word = decrypt_word(encrypted_word, key)
            decrypted_words.append(decrypted_word)

            if len(decrypted_words) == 3 or (len(decrypted_words) == len(encrypted_words) and len(encrypted_words) < 3):
                are_valid = check_for_valid_words(decrypted_words)

                if not are_valid:
                    decrypted_words = []
                    continue

                else:
                    right_key = key


        if right_key != 0:
            break
			
    decrypted_text = concat_decrypted_words(decrypted_words)

    print(decrypted_text)
    print(f"key: {right_key}")


def concat_decrypted_words(decrypted_words):

    result_text = ""

    for word in decrypted_words:
        result_text += word
        result_text += " "		

    return result_text.strip()


def check_for_valid_words(decrypted_words):

    for word in decrypted_words:

        tokenizer = RegexpTokenizer(r'\w+')
        lemma = WordNetLemmatizer()

        word_token = tokenizer.tokenize(word)[0]
        lemma_word = lemma.lemmatize(tokenizer.tokenize(word)[0])	

        if not wordnet.synsets(lemma_word) and word_token.lower() not in words.words():
            return False

    return True


def decrypt_word(encrypted_word, key):
    decrypted_word = ""

    for encrypted_letter in encrypted_word:
        decrypted_letter = ord(encrypted_letter)

        if UPPERCASE_A <= decrypted_letter <= UPPERCASE_Z:
            decrypted_letter -= key

            if not (UPPERCASE_A <= decrypted_letter <= UPPERCASE_Z):
                decrypted_letter += ALPHABET_LENGTH

        if LOWERCASE_A <= decrypted_letter <= LOWERCASE_Z:
            decrypted_letter -= key

            if not (LOWERCASE_A <= decrypted_letter <= LOWERCASE_Z):
                decrypted_letter += ALPHABET_LENGTH



        decrypted_word += chr(decrypted_letter)

    return decrypted_word


decrypt_text()
