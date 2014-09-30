import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers = test.strip().split(' ')
    numbers = sorted(numbers, key=lambda x: float(x))
    for number in numbers:
        print number,
    print ''

test_cases.close()
