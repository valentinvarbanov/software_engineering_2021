import os

def get_homeworks():
    # arr = next(os.walk("./"))[1]
    subfolders = [ f.path for f in os.scandir("./") if f.is_dir() ]
    return subfolders
    # for i in os.walk("./")[1]:
        # print(os.path.isdir(i))

print(get_homeworks())

for hw in get_homeworks():
    print(f"========= {hw} ===========")
    os.system(f'echo "It Works!" | python encrypt.py --key 3 > encrypted && cat encrypted | python {hw}/decrypt.py')
    print(f"========================================")

