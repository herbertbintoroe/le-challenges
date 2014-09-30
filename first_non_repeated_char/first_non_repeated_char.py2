"""
FIRST NON-REPEATED CHARACTER
CHALLENGE DESCRIPTION:

    Write a program to find the first non repeated character in a string.

    INPUT SAMPLE:

        The first argument will be a path to a filename containing strings. E.g.

        yellow
        tooth
        OUTPUT SAMPLE:

            Print to stdout, the first non repeating character, one per line. E.g.

            y
            h
"""

import sys

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'need a path to the file'
        sys.exit(-1)
    else:
        filename = sys.argv[1]

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            le_dict = {}
            non_repeat_char = ''
            for char in line:
                if char in le_dict:
                    le_dict[char] += 1
                    continue
                else:
                    non_repeat_char = char
                    le_dict[char] = 1

            for char in line:
                if le_dict[char] == 1:
                    print char
                    break

