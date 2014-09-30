import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    char_list = test.split(' ')
    index = int(char_list[-1])
    list_length = len(char_list) - 1
    if index > list_length:
        continue
    print char_list[list_length - index]

test_cases.close()
