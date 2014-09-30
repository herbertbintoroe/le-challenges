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
            (a, b, n) = line.split(" ")
            (a, b, n) = (int(a), int(b), int(n))

            buzzwords = ""
            for i in xrange(1, n+1):
                if i % a == 0:
                    if i % b == 0:
                        buzzwords += "FB "
                    else:
                        buzzwords += "F "
                elif i % b == 0:
                    buzzwords += "B "
                else:
                    buzzwords += str(i) + " "

            print buzzwords

