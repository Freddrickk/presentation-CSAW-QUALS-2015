import string
import random
from base64 import b64encode, b64decode

FLAG = 'flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'
f = open('./flag.enc', 'r')
FLAG = f.read()
f.close()

enc_ciphers = ['rot13', 'b64e', 'caesar']
dec_ciphers = ['rot13', 'b64d', 'caesard']

def rot13(s):
    _rot13 = string.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
    )
    return string.translate(s, _rot13)

def b64e(s):
    return b64encode(s)

def b64d(s):
    return b64decode(s)

def caesar(plaintext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def caesard(plaintext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = 'xyzabcdefghijklmnopqrstuvw'
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def encode(pt, cnt=50):
    tmp = '2{}'.format(b64encode(pt))
    for cnt in xrange(cnt):
        c = random.choice(enc_ciphers)
        i = enc_ciphers.index(c) + 1
        _tmp = globals()[c](tmp)
        tmp = '{}{}'.format(i, _tmp)

    return tmp

def decode(flag):
    while flag[0] in ['1', '2', '3']:
        c = dec_ciphers[int(flag[0]) - 1]
        flag = globals()[c](flag[1:])
    
    return flag


if __name__ == '__main__':
    print decode(FLAG)
