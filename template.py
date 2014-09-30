"""
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
