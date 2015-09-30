import copy
import string


def transform_input(input_vector):
    result = 0 # pas sur de 0
    index2 = 0
    
    while True:
        size = len(input_vector)

        if not index2 < size:
            break
        
        single_input = input_vector[index2]
        result += ord(single_input) & 0xffffffff
        index2 += 1

    return result & 0xffffffff


def sanitize_input(input_str, test_index):
    output_vector = []
    secret = [0xd600000064, 0x10a000000d6, 0x1710000010a, 0x1a100000171, 0x20f000001a1, 0x26e0000020f,0x2dd0000026e,0x34f000002dd,0x3ae0000034f,0x41e000003ae,0x4520000041e,0x4c600000452,0x538000004c6,0x5a100000538,0x604000005a1,0x63500000604,0x69600000635,0x70400000696,0x76300000704,0x7cc00000763,0x840000007cc,0x87500000840,0x8d400000875,0x920000008d4,0x96c00000920,0x9c20000096c,0xa0f000009c2,0xa0f]

    index = 0
    while 1:
        my_char = input_str[index]

        output_vector.append(my_char)
        key_dword = secret[index]
        new_vector = copy.deepcopy(output_vector)
        result = transform_input(new_vector)

        if result == (key_dword & 0xffffffff):
            if index == test_index:
                break

            if index == 0x1c:
                break
        else:
            raise SyntaxError()

        index += 1

    return ((index << 8) & 0x147)

password = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']

for i in range(28):
    for c in string.printable:
        try:
            password[i] = c
            sanitize_input(password, i)
            break
        except SyntaxError:
            continue

print ''.join(password)


