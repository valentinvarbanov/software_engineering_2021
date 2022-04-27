"""
Code.py
"""

import os
import csv


ENCRYPTION_KEY_KEY = 'key'
TEXT_KEY = 'data'
NAME_KEY = 'name'

verification_data = [
    {
        NAME_KEY: 'sample',
        ENCRYPTION_KEY_KEY : 3,
        TEXT_KEY: 'It works!',
    },
    {
        NAME_KEY: 'easy',
        ENCRYPTION_KEY_KEY : 19,
        TEXT_KEY: 'can not go any simpler than this',
    },
    {
        NAME_KEY: 'medium',
        ENCRYPTION_KEY_KEY : 23,
        TEXT_KEY: 'Will CaPiTaLiZaTiOn break the homework',
    },
    {
        NAME_KEY: 'special',
        ENCRYPTION_KEY_KEY : 13,
        TEXT_KEY: 'Or $p3c1al characters? Let\'s find out...',
    },
    {
        NAME_KEY: 'advanced',
        ENCRYPTION_KEY_KEY : 7,
        TEXT_KEY: 'AI Dungeon is a free-to-play\
         single-player and multiplayer\
        text adventure game which uses \
        artificial intelligence to generate \
        content. It allows players to create\
         and share their own custom adventure\
         settings. The game\'s first version was made available on Colab in May\
          2019, and its second version (initially called AI Dungeon 2) was \
          released online and for iOS and Android in December 2019. The AI \
          model was then upgraded in July 2020.',
    }
]

#pylint: disable=E0001
#pylint: disable=R1732
#pylint: disable=W1514
output_file = open('./results.csv', 'w')
writer = csv.writer(output_file)
header = ['name']

for data_set in verification_data:
    header.append(data_set[NAME_KEY])
    header.append(f'{data_set[NAME_KEY]} key')

writer.writerow(header)


def get_homeworks():
    """
    Function ffor getting homeworks
    """
    subfolders = [ f.path for f in os.scandir("./") if f.is_dir() ]
    return subfolders

print(get_homeworks())

for hw in get_homeworks():

    name = hw
    name_components = hw.split('_')

    if len(name_components) == 3:
        first = name_components[1].capitalize()
        last = name_components[2].capitalize()
        name = f'{first} {last}'

    csv_row = [name]

    print(f'----- {name} -----')

    for data_set in verification_data:
        KEY = data_set[ENCRYPTION_KEY_KEY]
        TEXT = data_set[TEXT_KEY]

        decrypted_output = os.popen(f'echo "{TEXT}" | \
        python encrypt.py --key "{KEY}" > encrypted && cat encrypted |\
         python {hw}/decrypt.py').read()

        DECRIPTION_SUCCESS = 0
        KEY_DISCOVERED = 0

        if TEXT in decrypted_output:
            DECRIPTION_SUCCESS = 1

        if f'key: {KEY}' in decrypted_output:
            KEY_DISCOVERED = 1
        csv_row.append(DECRIPTION_SUCCESS)
        csv_row.append(KEY_DISCOVERED)

        print(f'{data_set[NAME_KEY]}: key({KEY_DISCOVERED}) \
        text({DECRIPTION_SUCCESS})')
        print(f'==>{decrypted_output}<==')

    writer.writerow(csv_row)

output_file.close()
