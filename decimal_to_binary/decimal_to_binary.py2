"""
DECIMAL TO BINARY

CHALLENGE DESCRIPTION:

    Given a decimal (base 10) number, print out its binary representation.

    INPUT SAMPLE:
        Your program should accept as its first argument a path to a filename containing whole decimal numbers greater or equal to 0, one per line. 
        Ignore all empty lines. E.g.

        2
        10
        67

    OUTPUT SAMPLE:

        Print the binary representation, one per line. E.g.

        10
        1010
        1000011
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
            print "{0:b}".format(int(line))
