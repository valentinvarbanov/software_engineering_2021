import os
import subprocess
import csv


encryption_key_key = 'key'
text_key = 'data'
name_key = 'name'

verification_data = [
    {
        name_key: 'sample',
        encryption_key_key : 3,
        text_key: 'It works!',
    },
    {
        name_key: 'easy',
        encryption_key_key : 19,
        text_key: 'can not go any simpler than this',
    },
    {
        name_key: 'medium',
        encryption_key_key : 23,
        text_key: 'Will CaPiTaLiZaTiOn break the homework',
    },
    {
        name_key: 'special',
        encryption_key_key : 13,
        text_key: 'Or $p3c1al characters? Let\'s find out...',
    },
    {
        name_key: 'advanced',
        encryption_key_key : 7,
        text_key: 'AI Dungeon is a free-to-play single-player and multiplayer text adventure game which uses artificial intelligence to generate content. It allows players to create and share their own custom adventure settings. The game\'s first version was made available on Colab in May 2019, and its second version (initially called AI Dungeon 2) was released online and for iOS and Android in December 2019. The AI model was then upgraded in July 2020.',
    }
]

output_file = open('./results.csv', 'w')
writer = csv.writer(output_file)
header = ['name']

for data_set in verification_data:
    header.append(data_set[name_key])
    header.append(f'{data_set[name_key]} key')

writer.writerow(header)

def get_homeworks():
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
        key = data_set[encryption_key_key]
        text = data_set[text_key]

        decrypted_output = os.popen(f'echo "{text}" | python encrypt.py --key "{key}" > encrypted && cat encrypted | python {hw}/decrypt.py').read()

        decryption_success = 0
        key_discovered = 0

        if text in decrypted_output:
            decryption_success = 1
        
        if f'key: {key}' in decrypted_output:
            key_discovered = 1

        csv_row.append(decryption_success)
        csv_row.append(key_discovered)

        print(f'{data_set[name_key]}: key({key_discovered}) text({decryption_success})')
        print(f'==>{decrypted_output}<==')

    writer.writerow(csv_row)

output_file.close()