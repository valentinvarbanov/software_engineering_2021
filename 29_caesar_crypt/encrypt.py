import sys


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

def main(argv=sys.argv[1:]):
    if len(argv) > 0:
        try:
            key = int(argv[0])
            if not 0 < key < 26:
                print("Not valid number")
                exit(-2)
        except ValueError:
            print("This is not valid key")
            exit(-1)
    if len(argv) == 1:
        try:
            str = input()
            while str  is not None:
                print(encrypt(str, int(argv[0])))
                str = input()
        except EOFError:
            pass
    elif len(argv) == 2:
        f = open(argv[1], "r")
        print(encrypt(f.read(), int(argv[0])))
        f.close()
    elif len(argv) == 3:
        f = open(argv[1], "r")
        newFile = open(argv[2], "w")
        newFile.write(encrypt(f.read(), int(argv[0])))
        f.close()
        newFile.close()
    else:
        exit(-1)



# print(encrypt_single_char('A', 3))
# print(encrypt_single_char('Z', 3))
# print(encrypt_single_char('a', 3))
# print(encrypt_single_char('z', 3))
# print(encrypt_single_char('!', 3))

main()