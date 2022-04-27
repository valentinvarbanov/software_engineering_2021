
import sys
import nltk


def decrypt(string, key):
    result = ""

    for i in string:
        result += decrypt_single(i, key)

    return result


def decrypt_single(symbol, key):
    A_INTEGER = ord('A')
    Z_INTEGER = ord('Z')
    a_INTEGER = ord('a')
    z_INTEGER = ord('z')

    symbol_integer = ord(symbol)
    result = symbol_integer
    difference = (Z_INTEGER - A_INTEGER) + 1

    if A_INTEGER <= symbol_integer <= Z_INTEGER:
        result += key
        if not (A_INTEGER <= result <= Z_INTEGER):
            result += difference
    elif a_INTEGER <= symbol_integer <= z_INTEGER:
        result -= key
        if not (a_INTEGER <= result <= z_INTEGER):
            result += difference

    return chr(result)


def main():
    input_sen = []
    key = 0
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        for k in line.split(' '):
            input_sen.append(k)
    while True:
        key += 1
        dec = decrypt(dec, 1)
        if dec.lower() in english_vocab:
            break
        if (key > 26):
            break
    if len(input_sen) > 1:
        dec = decrypt(dec, key)
        if dec.lower() not in english_vocab:
            while dec.lower() not in english_vocab:
                key += 1
                dec = decrypt(dec, 1)
                if key > 26:
                    break

    res = []
    for dec in input_sen:
        res.append(decrypt(dec, key))
    print(' '.join(res) + "key: " + str(26 - key))


main()