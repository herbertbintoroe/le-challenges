"""
INTERRUPTED BUBBLE SORT
CHALLENGE DESCRIPTION:

    Bubble sort is the simplest algorithm for elements sorting. At each iteration we sequentially compare values of subsequent elements and swap them if necessary.

    Your job is to write a program which finds a state of a given list of positive integer numbers after applying a given count of bubble sort iterations.

    INPUT SAMPLE:

        Your program should accept as its first argument a path to a filename. Each line in this file contains a space-separated list of positive integers and ends with a number of iterations, separated by vertical line |. E.g.:

            36 47 78 28 20 79 87 16 8 45 72 69 81 66 60 8 3 86 90 90 | 1
            40 69 52 42 24 16 66 | 2
            54 46 0 34 15 48 47 53 25 18 50 5 21 76 62 48 74 1 43 74 78 29 | 6
            48 51 5 61 18 | 2
            59 68 55 31 73 4 1 25 26 19 60 0 | 2

    OUTPUT SAMPLE:

        Print to stdout the state of given lists after applying a given count of bubble sort iterations. E.g.:

            36 47 28 20 78 79 16 8 45 72 69 81 66 60 8 3 86 87 90 90
            40 42 24 16 52 66 69
            0 15 25 18 34 5 21 46 47 48 48 1 43 50 53 29 54 62 74 74 76 78
            5 48 18 51 61
            55 31 59 4 1 25 26 19 60 0 68 73
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
            (numbers, iteration) = line.split('|')
            iteration = int(iteration.strip())
            # Start le code
            number_list = numbers.strip().split(' ')
            number_list = map(int, number_list)

            for j in xrange(0, min(iteration, len(number_list)-1)):
                for i in xrange(0, len(number_list)-1):
                    if number_list[i] > number_list [i+1]:
                        number_list[i], number_list[i+1] = number_list[i+1], number_list[i]

            number_list = map(str, number_list)
            print ' '.join(number_list)
