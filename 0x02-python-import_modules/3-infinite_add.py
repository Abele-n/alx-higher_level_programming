#!/usr/bin/python3

if __name__ == "__main__":
    """addition of all elements"""
    import sys

    total_no = 0
    for m in range(len(sys.argv) - 1):
        total_no += int(sys.argv[m + 1])
        print("{}".format(total_no))
