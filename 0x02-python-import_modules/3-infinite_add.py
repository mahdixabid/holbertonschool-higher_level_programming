#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    sum = 0
    for x in range(0, len(argv)):
        if (x > 0):
            sum = sum + int(argv[x])
    print("{}".format(sum))
