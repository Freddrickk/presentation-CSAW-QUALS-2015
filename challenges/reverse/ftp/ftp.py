import string
import copy
import itertools
import sys
import string
	

def single_decrypt_attempt():
    result_key = 5381
    key = 3548828169
    password = ""

    while key != result_key:
        for c in string.printable:
            print key
            if key <= 0:
                sys.exit()
            if ((key - ord(c)) % 33) == 0:
                password += c
                key -= ord(c)
                key /= 33
                break

    print password


def backtrack(password, key):
    result_key = 5381
    if key == result_key:
        print password[::-1]
        return password

    for c in string.printable:

        if (((key - ord(c)) % 33) == 0) and (((key - ord(c))/33) >= result_key):
            password1 = copy.deepcopy(password)
            key1 = copy.deepcopy(key)

            password1.append(c)

            key1 -= ord(c)
            key1 /= 33

            result = backtrack(password1, key1)

            if result:
                return result

    return False


for i in range(10000000):
    password = []
    key = 3548828169
    key += (i * 0x100000000)
    response = backtrack(password, key)
    if response:
        print response
