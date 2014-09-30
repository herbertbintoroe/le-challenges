"""
REVERSE WORDS
CHALLENGE DESCRIPTION:

    Write a program to reverse the words of an input sentence.

    INPUT SAMPLE:

        The first argument will be a path to a filename containing multiple sentences, one per line. Possibly empty lines too. E.g.

        Hello World
        Hello CodeEval
        OUTPUT SAMPLE:

    Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print.__ E.g.

            World Hello
            CodeEval Hello
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

            # Start le code
            word_list = line.split(' ')
            print ' '.join(word_list[::-1])
