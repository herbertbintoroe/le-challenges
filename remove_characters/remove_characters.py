"""
REMOVE CHARACTERS

CHALLENGE DESCRIPTION:

    Write a program to remove specific characters from a string.

    INPUT SAMPLE:

        The first argument will be a path to a filename containing an input string followed by a comma and then the characters that need to be scrubbed. E.g.

        how are you, abc
        hello world, def

    OUTPUT SAMPLE:

        Print to stdout, the scrubbed strings, one per line. Trim out any leading/trailing whitespaces if they occur. E.g.

        how re you
        hllo worl
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

            (words, chars) = line.split(',')
            char_list = list(chars.strip())
            scrubbed_words = ''
            for le_char in words:
                if le_char not in char_list:
                    scrubbed_words += le_char

            print scrubbed_words.strip()
