import sys
import argparse

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

def main():

    parser = argparse.ArgumentParser(
        description='Encrypt text in a file.')
    parser.add_argument('--key', '-k', type=int, dest='key',
                    help='options for the keys')
    parser.add_argument('--input', '-i', dest='filename',
                    help = 'options for the filename')
    # parser.add_argument('strings', metavar='N', type=str, nargs='+',
    #                 help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                 const=sum, default=max,
    #                 help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.key)
#print(args.accumulate(args.integers))

    try:
        if not 0 < args.key < 26:
            print('Not a valid number!')
            exit(-2)
        if not args.filename:
            str = input()

            while str is not None:
                print(encrypt(str, int(args.key)))
                str = input()
        else:
            with open(args.filename, 'r') as file:
                print(encrypt(file.read(), args.key))
    except ValueError:
        print('This is not a valid key!')
        exit(-1)
    except EOFError:
        print('The program terminated!')
        exit(-3)

    # if len(argv) == 1:
    #     try:
    #         str = input()
    #         while str  is not None:
    #             print(encrypt(str, int(argv[0])))
    #             str = input()
    #     except EOFError:
    #         pass
    # elif len(argv) == 2:
    #     f = open(argv[1], "r")
    #     print(encrypt(f.read(), int(argv[0])))
    #     f.close()
    # elif len(argv) == 3:
    #     f = open(argv[1], "r")
    #     newFile = open(argv[2], "w")
    #     newFile.write(encrypt(f.read(), int(argv[0])))
    #     f.close()
    #     newFile.close()
    # else:
    #     exit(-1)



# print(encrypt_single_char('A', 3))
# print(encrypt_single_char('Z', 3))
# print(encrypt_single_char('a', 3))
# print(encrypt_single_char('z', 3))
# print(encrypt_single_char('!', 3))

main()