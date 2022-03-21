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

print(encrypt_single_char('A', 3))
print(encrypt_single_char('Z', 3))
print(encrypt_single_char('a', 3))
print(encrypt_single_char('z', 3))
print(encrypt_single_char('!', 3))

print(encrypt(input(), 3))

