import os
import subprocess
import csv

hw_sample_text = "It works!"
hw_sample_key = 3

echoMessage = "AI Dungeon is a free-to-play single-player and multiplayer text adventure game which uses artificial intelligence to generate content. It allows players to create and share their own custom adventure settings. The game's first version was made available on Colab in May 2019, and its second version (initially called AI Dungeon 2) was released online and for iOS and Android in December 2019. The AI model was then upgraded in July 2020."

key = 7

f = open('./results.csv', 'w')
writer = csv.writer(f)
header = ["name", "message 1", "key 1", "message 2", "key 2"]

writer.writerow(header)

def get_homeworks():
    # arr = next(os.walk("./"))[1]
    subfolders = [ f.path for f in os.scandir("./") if f.is_dir() ]
    return subfolders
    # for i in os.walk("./")[1]:
        # print(os.path.isdir(i))

print(get_homeworks())

for hw in get_homeworks():
    sample_message_found = 0
    sample_key_found = 0
    checkMessage = 0
    checkKey = 0
    print(f"========= {hw} ===========")
  
    decrypted_output = os.popen(f'echo "{hw_sample_text}" | python encrypt.py --key "{hw_sample_key}" > encrypted && cat encrypted | python {hw}/decrypt.py').read()
    
    print("decrypted:")
    print(decrypted_output)

    if hw_sample_text in decrypted_output:
        sample_message_found = 1
        print("Sample message decrypted successfully.")

    if f"key: {hw_sample_key}" in decrypted_output:
        sample_key_found = 1
        print("Sample key discovered.")

    echo = os.popen(f'echo "{echoMessage}" | python encrypt.py --key "{key}" > encrypted && cat encrypted | python {hw}/decrypt.py').read()
    
    print("decrypted:")
    print(echo)

    if echoMessage in echo:
        checkMessage = 1
        print("Message decrypted successfully.")

    if f"key: {key}" in echo:
        checkKey = 1
        print("Key was discovered.")

    data = [hw, sample_message_found, sample_key_found, checkMessage, checkKey]

    writer.writerow(data)

    
    print(f"========================================")

f.close()