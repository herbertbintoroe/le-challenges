"""
SUM OF INTEGERS FROM FILE
CHALLENGE DESCRIPTION:


    Print out the sum of integers read from a file.close
    INPUT SAMPLE:

        The first argument to the program will be a path to a filename containing a positive integer, one per line. E.g.

        5
        12
        OUTPUT SAMPLE:

            Print out the sum of all the integers read from the file. E.g.

            17
"""

import sys

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'need a path to the file'
        sys.exit(-1)
    else:
        filename = sys.argv[1]

    with open(filename) as f:
        count = 0
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                count += int(line)
            except ValueError:
                continue

        print count

