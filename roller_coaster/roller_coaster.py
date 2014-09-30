import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count = 0
    for letter in test:
        if letter == ' ':
            sys.stdout.write(' ')
            continue
        elif count % 2 == 0:
            sys.stdout.write(letter.upper())
        else:
            sys.stdout.write(letter.lower())
        count += 1
    print ''

test_cases.close()
