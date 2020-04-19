from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os, argparse

def hash_key(key):
    return SHA256.new(key.encode()).digest()

key = 'awesome'
block_size = 64*1024

def decryption(filename, key):
    decryptor = AES.new(hash_key(key), AES.MODE_ECB)
    print(os.getcwd(), filename)
    if filename.startswith('encrypted%%%'):
        outname = filename[12:]
    else:
        return
    with open(filename, 'rb') as infile:
        with open(outname, 'wb') as outfile:
            filesize = int(infile.read(16))
            while True:
                data = infile.read(block_size)
                if len(data) == 0:
                    break
                outfile.write(decryptor.decrypt(data))
                outfile.truncate(filesize)
    os.remove(filename)

def ransomdecryption():
    pwd = os.getcwd()
    files = list(os.walk(pwd))[0][2]
    files.remove('you_are_freed.py')
    for each in files:
        decryption(each, key)
    folders = list(os.walk(pwd))[0][1]
    print('folders:', folders)
    for folder in folders:
        print('working on ', folder)
        os.chdir(os.path.join(pwd, folder))
        print(os.getcwd())
        files = list(os.walk(os.getcwd()))[0][2]
        print(f'{folder} --> {files}')
        for each in files:
            decryption(each, key)
        os.chdir(pwd)
    os.remove('you_are_freed.py')

ransomdecryption()
