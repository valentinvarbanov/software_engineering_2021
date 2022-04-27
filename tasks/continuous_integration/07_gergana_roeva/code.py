# pylint: disable=C0301
# pylint: disable=C0303
# pylint: disable=C0114
# pylint: disable=C0116

import os
import csv

ENCRYPTION_KEY_KEY = 'key'
TEXT_KEY = 'data'
NAME_KEY = 'name'

VERIFICATON_DATA = [
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
        TEXT_KEY: 'AI Dungeon is a free-to-play single-player and multiplayer text adventure game which uses artificial intelligence to generate content. It allows players to create and share their own custom adventure settings. The game\'s first version was made available on Colab in May 2019, and its second version (initially called AI Dungeon 2) was released online and for iOS and Android in December 2019. The AI model was then upgraded in July 2020.',
    }
]

OUTPUT_FILE = open('./results.csv', 'w')
WRITER = csv.writer(OUTPUT_FILE)
HEADER = ['name']

for data_set in VERIFICATON_DATA:
    HEADER.append(data_set[NAME_KEY])
    HEADER.append(f'{data_set[NAME_KEY]} key')

WRITER.writerow(HEADER)

def get_homeworks():
    subfolders = [f.path for f in os.scandir("./") if f.is_dir()]
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

    for data_set in VERIFICATON_DATA:
        key = data_set[ENCRYPTION_KEY_KEY]
        text = data_set[TEXT_KEY]

        decrypted_output = os.popen(f'echo "{text}" | python encrypt.py --key "{key}" > encrypted && cat encrypted | python {hw}/decrypt.py').read()

        decryption_success = 0
        key_discovered = 0

        if text in decrypted_output:
            decryption_success = 1
        
        if f'key: {key}' in decrypted_output:
            key_discovered = 1

        csv_row.append(decryption_success)
        csv_row.append(key_discovered)

        print(f'{data_set[NAME_KEY]}: key({key_discovered}) text({decryption_success})')
        print(f'==>{decrypted_output}<==')

    WRITER.writerow(csv_row)

OUTPUT_FILE.close()
