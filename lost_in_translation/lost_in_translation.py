import sys

CHAR_MAPPING = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    # 'g': 'g',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    # 'l': 'v',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q',
}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for char in test.strip():
        if char == ' ':
            sys.stdout.write(' ')
        else:
            sys.stdout.write(CHAR_MAPPING[char])
    print ''

test_cases.close()
