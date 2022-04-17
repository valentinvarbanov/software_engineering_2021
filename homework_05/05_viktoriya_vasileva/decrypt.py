import sys
import nltk



def encrypt(string, key):
    result = ""
    
    for i in string:
        result += encrypt_single_char(i, key)

    return result

def encrypt_single_char(symbol, key):
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
            result -= difference
    elif a_INTEGER <= symbol_integer <= z_INTEGER:
        
        result += key
        if not (a_INTEGER <= result <= z_INTEGER):
            result -= difference

    return chr(result)

def remove_disallowed_charecters(m):
    disallowed_char = "._!"
    for character in disallowed_char:
        m = m.replace(character, "")
    m = m.replace("\n", "")
    return m


def main():
    msg = []
    key = 0
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        for l in line.split(' '):
            msg.append(l)
    m = remove_disallowed_charecters(msg[0])
    while True:
        key += 1
        m = encrypt(m, 1)
        if m.lower() in english_vocab:
            break
        if(key > 27):
            break
    if len(msg) > 1:
        m = remove_disallowed_charecters(msg[1])
        m = encrypt(m, key)
        if m.lower() not in english_vocab:
            while m.lower() not in english_vocab:
                key += 1
                m = encrypt(m, 1)
                if key > 27:
                    break

    res = []
    for m in msg:
        res.append(encrypt(m, key))
    print(' '.join(res)+"key: " + str(26-key))

main()
# print(encrypt("zebra", 3)) #
# print(encrypt(encrypt("zebra", 3), 23)) # works 
# print(encrypt(encrypt("zebra", 3), -3)) # does not work > "Febra" "may" > "maE"
# print(encrypt("may", 2))
# print(encrypt(encrypt("may", 2), 24))


