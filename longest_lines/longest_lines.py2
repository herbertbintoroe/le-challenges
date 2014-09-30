"""
LONGEST LINES
CHALLENGE DESCRIPTION:


    Write a program to read a multiple line text file and write the 'N' longest lines to stdout. Where the file to be read is specified on the command line.

    INPUT SAMPLE:

        Your program should read an input file (the first argument to your program will be a path to a filename). The first line contains the value of the number 'N' followed by multiple lines. You may assume that the input file is formatted correctly and the number on the first line i.e. 'N' is a valid positive integer. E.g.

        2
        Hello World
        CodeEval
        Quick Fox
        A
        San Francisco

        OUTPUT SAMPLE:

            The 'N' longest lines, newline delimited. Ignore all empty lines in the input.__ Ensure that there are no trailing empty spaces on each line you print. Also ensure that the lines are printed out in decreasing order of length i.e. the output should be sorted based on their length. E.g.

            San Francisco
            Hello World

"""

import sys

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'need a path to the file'
        sys.exit(-1)
    else:
        filename = sys.argv[1]

    with open(filename) as f:
        line_num = 0
        num_words = 0
        word_list = []
        word_dict = {}
        for line in f:
            line = line.strip()
            if line_num == 0:
                num_words = int(line)
                line_num += 1

            if not line:
                continue
            # Start le code
            word_dict[line] = len(line)
            word_list.append(line)

        new_word_list = sorted(word_dict, key=lambda key:word_dict[key], reverse=True)
        for i in xrange(0, num_words):
            print new_word_list[i]
