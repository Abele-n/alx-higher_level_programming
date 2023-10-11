#!/usr/bin/python3
"""computes metrics as it reads from standard input
After 10 lines or input from keyboard, interruption (CTRL + C)
prints the following statistics:
    -Total size up to that point
    -the number of read status upto that point
"""


def print_stats(size, status_codes):
    """prints all the metrics

    Args:
    size(int): the read file size
    status_codes(dict): accumulated count of status codes
    """

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}:{}".format(key, status_codes[key])

    if __name__ = "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '405', '500']
    my_count = 0

    try:
        for line in sys.stdin:
            if my_count == 10:
                print_stats(size, status_codes)
                my_count = 1
            else:
                my_count += 1
            line = line.split()
        try:
            if line[-2] in valid_codes:
                if status_codes.get(line[-2], -1) == -1:
                    status_codes[line[-2]] = 1
                else:
                    status_codes[line[-2]] += 1
        except IndexError:
            pass
            print_stats(size, status_codes
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
