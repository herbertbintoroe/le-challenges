"""
Fibonacci Series Challenge

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1. Given a positive integer 'n', print out the F(n).

INPUT SAMPLE:

The first argument will be a path to a filename containing a positive integer, one per line. E.g.

5
12

OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

5
144
"""

import sys


def fib(number):
    a = 0
    b = 1
    for i in xrange(0, number):
        a, b = b, a+b
    return a


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
                print "%s is not a valid number" % line
                continue

            fib_number = fib(number)
            print fib_number
