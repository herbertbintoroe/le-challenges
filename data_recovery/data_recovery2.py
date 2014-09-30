"""
DATA RECOVERY
CHALLENGE DESCRIPTION:

    Your friends decided to make a fun of you. They've installed a script to your computer which shuffled all of the words within a text. It was a joke, so they've left hints for each sentence which allow you to easily rebuild your data. The challenge is to write a program which reconstructs each sentence out of a set of words, you need to find out how to use a given hint and print out the original sentences.

    INPUT SAMPLE:

        Your program should accept as its first argument a path to a filename. Each line is a test case. Each test case consists of a set of words and a sequence of numbers separated by a semicolon. The words within a set and the numbers within a sequence are separated by a single whitespace. E.g.

        2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 
        2
        programming first The language;3 2 1
        programs Manchester The written ran Mark 1952 1 in Autocode from;6 
        2 1 7 5 3 11 4 8 9
        OUTPUT SAMPLE:

            For each test case print out the reconstructed sentence one per line. E.g.

            However, it was not implemented until 1998 and 2000
            The first programming language
            The Manchester Mark 1 ran programs written in Autocode from 1952
            Constraints: 
                The number of test cases is in range [20, 40]. 
                The words consist of ASCII upper and lower case letters, digits and punctuation.
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
            # (words, orders) = line.split(';')
            word_list = line.split(';')[0].split(' ')
            order_list = line.split(';')[1].split(' ')

            for i in xrange(1, len(word_list) + 1):
                if str(i) not in order_list:
                    order_list.append(i)

            words_order_dict = {}
            count = 0
            for i in order_list:
                words_order_dict[str(i)] = word_list[count]
                count += 1

            le_sentence = ''
            for i in xrange(1, len(words_order_dict)+1):
                le_sentence += words_order_dict[str(i)] + " "

            print le_sentence
