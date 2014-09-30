import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    for word in test.split(' '):
        new_word = ''
        should_cap = True
        for letter in word:
            if should_cap:
                new_word += letter.upper()
                should_cap = False
            else:
                new_word += letter
        print new_word,

test_cases.close()
