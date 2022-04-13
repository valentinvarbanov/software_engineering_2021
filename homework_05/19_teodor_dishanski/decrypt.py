# Teodor Dishanski, XII B, Number 19
# Technology School Electronic Systems

"""Module to decrypt a message encrypted via brute force."""

import sys
import nltk

from nltk.corpus import wordnet


def decrypt_single_char(char, key):
    """Decrypt a single char with a given key."""
    assert isinstance(char, str)
    assert isinstance(key, int)

    upper_a_integer = ord('A')
    upper_z_integer = ord('Z')
    lower_a_integer = ord('a')
    lower_z_integer = ord('z')

    char_integer = ord(char)
    result = char_integer
    difference = (upper_z_integer - upper_a_integer) + 1

    if upper_a_integer <= char_integer <= upper_z_integer:
        result -= key
        if not upper_a_integer <= result <= upper_z_integer:
            result += difference
    elif lower_a_integer <= char_integer <= lower_z_integer:
        result -= key
        if not lower_a_integer <= result <= lower_z_integer:
            result += difference

    return chr(result)


def decrypt_single_word(word, key, space_flag):
    """Decrypt a whole string with a given key."""
    assert isinstance(word, str)
    assert isinstance(key, int)
    assert isinstance(space_flag, bool)

    decrypted_word = ''

    assert isinstance(word, str)
    assert isinstance(key, int)
    assert isinstance(space_flag, bool)

    for char in word:
        condition_upper = (65 <= ord(char) <= 90)
        condition_lower = (97 <= ord(char) <= 122)

        if condition_upper or condition_lower:
            decrypted_word += decrypt_single_char(char, key)
        else:
            decrypted_word += char

    return decrypted_word + ' ' if space_flag else decrypted_word


def find_possible_keys(word):
    """Look for possible keys for every single word."""
    possible_keys = set()

    for i in range(1, 26):
        correct_word = ''

        for char in word:
            condition_upper = (65 <= ord(char) <= 90)
            condition_lower = (97 <= ord(char) <= 122)

            if condition_upper or condition_lower:
                correct_word += decrypt_single_char(char, i)

        if wordnet.synsets(correct_word):
            possible_keys.add(i)

    return possible_keys


def find_encryption_key(sets_keys):
    """Find a specific encryption key for the whole message."""
    intersection_sets = set()

    for set_key in sets_keys:
        if len(set_key) != 0:
            if len(intersection_sets) == 0:
                intersection_sets |= set_key
            else:
                intersection_sets &= set_key

    if len(intersection_sets) == 0:
        list_keys = [list(element) for element in sets_keys]
        list_keys = [element for set_keys in list_keys for element in set_keys]
        return nltk.FreqDist(list(list_keys)).max()

    return list(intersection_sets)[0]


def manage_input():
    """Read the input stream."""
    all_words = []
    lines = []

    while True:
        line = sys.stdin.readline()

        if not line:
            break

        lines.append(line)

    for i, _ in enumerate(lines):
        words = lines[i].split(' ')
        all_words.append(words)

    return all_words


def manage_output(all_words, key_encryption):
    """Write the output stream."""
    encrypted_message = ''

    for i, _ in enumerate(all_words):
        for j, _ in enumerate(all_words[i]):
            if j != len(all_words[i]) - 1:
                encrypted_message += decrypt_single_word(
                    all_words[i][j], key_encryption, True)
            else:
                encrypted_message += decrypt_single_word(
                    all_words[i][j], key_encryption, False)

    print(f"{encrypted_message}key: {key_encryption}")


def main():
    """Manage the logic of the brute force."""
    all_words = manage_input()
    sets_keys = []

    for i, _ in enumerate(all_words):
        for j, _ in enumerate(all_words[i]):
            sets_keys.append(find_possible_keys(all_words[i][j]))

    key_encryption = find_encryption_key(sets_keys)
    manage_output(all_words, key_encryption)


if __name__ == '__main__':
    main()
