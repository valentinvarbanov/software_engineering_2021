# Cryptography - Caesar Crypt

## Task

Use the code implemented in class as base and implement a brute force decryption algorithm.

The input should be provided on the standard input:

```bash
$ echo "It works!" | python encrypt.py 3 > encrypted
# WORKDIR is xx_firstname_lastname
$ cat encrypted | python decrypt.py
It works!
key: 3
```

You should come up with a custom algorithm that would detect if a key has successfully decrypted the input.

Hint: Check `wordnet` from `nltk` for recognition if the decrypted text is correct.

## Where to upload the homework?

Upload the source file named `decrypt.py` in a folder named `xx_firstname_lastname` in the current folder (`homework_05`) where:
- `xx` is your number in class
- `firstname` is your first name
- `lastname` is your last/family name

Example: `05_ivan_ivanov/decrypt.py`

Note: The homework would be graded automatically, any problem with the naming would lead to **zero** points.

## Code reviews

| Student | Reviewer 1 | Reviewer 2 |
|---------|------------|------------|
| Alexander1022 | AngelStoyanov33 | DeniBademi |
| AngelStoyanov33 | Martincho2003 | Teodor1331 |
| atanasatanasov03 | petardmnv | StelianRBG |
| Vic-Dim | StelianRBG | Ivan-Enchev |
| Vicktoria853 | DeniBademi | mvvrachev |
| Vladikolev0321 | VayerMaking | Alexander1022 |
| GerganaRoeva | Lilly7777 | atanasatanasov03 |
| DeniBademi | Vladikolev0321 | GerganaRoeva |
| elizadamgova | marto55 | Martincho2003 |
| Ivan-Enchev | elizadamgova | AngelStoyanov33 |
| Lilly7777 | mvvrachev | petardmnv |
| mvvrachev | atanasatanasov03 | Vicktoria853 |
| marto55 | Teodor1331 | elizadamgova |
| marti456 | Vicktoria853 | Vladikolev0321 |
| Martincho2003 | GerganaRoeva | Vic-Dim |
| VayerMaking | Alexander1022 | marti456 |
| petardmnv | Ivan-Enchev | VayerMaking |
| StelianRBG | Vic-Dim | Lilly7777 |
| Teodor1331 | marti456 | marto55 |

## Deadline

Uploading the homework:

```
Mon, 4 Apr 2022 23:59:59 +0300
```

Doing the code reviews and merging the PR (pull request):

```
Wed, 6 Apr 2022 23:59:59 +0300
```