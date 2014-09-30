"""
LONGEST COMMON SUBSEQUENCE
CHALLENGE DESCRIPTION:

    You are given two sequences. Write a program to determine the longest common subsequence between the two strings (each string can have a maximum length of 50 characters). NOTE: This subsequence need not be contiguous. The input file may contain empty lines, these need to be ignored.

    INPUT SAMPLE:
    The first argument will be a path to a filename that contains two strings per line, semicolon delimited. You can assume that there is only one unique subsequence per test case. E.g.

    XMJYAUZ;MZJAWXU

    OUTPUT SAMPLE:
    The longest common subsequence. Ensure that there are no trailing empty spaces on each line you print. E.g.

    MJAU
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
                word1, word2 = line.split(';')
            except ValueError:
                continue
            print "Input: word1 = %s, word2 = %s" % (word1, word2)


