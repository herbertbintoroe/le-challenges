"""
Number of Ones

Write a program to determine the number of 1 bits in the internal representation of a given integer.

INPUT SAMPLE:

    The first argument will be a path to a filename containing an integer, one per line. E.g.

    10
    22
    56

    OUTPUT SAMPLE:

    Print to stdout, the number of ones in the binary form of each number. E.g.

    2
    3
    3
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
            try:
                number = int(line)
            except ValueError:
                continue
            count = 0
            for i in "{0:b}".format(number):
                if int(i) == 1:
                    count += 1

            print count
