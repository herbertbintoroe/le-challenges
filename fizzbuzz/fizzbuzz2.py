import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    if not test:
        continue
    (a, b, n) = test.split(" ")
    (a, b, n) = (int(a), int(b), int(n))

    buzzwords = ""
    for i in xrange(1, n+1):
        if i % a == 0:
            if i % b == 0:
                buzzwords += "FB "
            else:
                buzzwords += "F "
        elif i % b == 0:
            buzzwords += "B "
        else:
            buzzwords += str(i) + " "

    print buzzwords

test_cases.close()
