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
    parser.add_argument('--output', '-o', dest='fileoutput',
                    help = 'options for the output file')

    args = parser.parse_args()

    fd_in = sys.stdin
    fd_out = sys.stdout

    if not 0 < args.key < 26:
        print('Not a valid number!')
        sys.exit(1)

    if args.filename:
        fd_in = open(args.filename, 'r')

    if args.fileoutput:
        fd_out = open(args.fileoutput, 'w')
    
    fd_out.write(encrypt(fd_in.read(), args.key))

    if fd_in != sys.stdin:
        fd_in.close()
    if fd_out != sys.stdout:
        fd_out.close()

main()