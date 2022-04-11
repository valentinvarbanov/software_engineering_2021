import string
from nltk.corpus import wordnet, words
from nltk import RegexpTokenizer, WordNetLemmatizer

def validate_word(word):
    tokenizer = RegexpTokenizer(r'\w+')
    lemma = WordNetLemmatizer()

    word_token = tokenizer.tokenize(word)[0]
    lemma_word = lemma.lemmatize(tokenizer.tokenize(word)[0])	

    if word_token.lower() in words.words() or wordnet.synsets(lemma_word):
        return True
    else:
        return False

def decrypt_with_shift(text, shift):
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    
    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter 
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)

def decrypt(text):
    for n in range(26):
        result = []
        msg = decrypt_with_shift(text, n)
        msg = msg.split()
        for i in msg:
            if validate_word(i):
                result.append(i)
            else:
                break
        if len(result) == len(msg):
            d = ""
            for w in result:
                d = d + " " + w
            print(d.strip())
            print(n)
 
message = input()
decrypt(message)