#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


def output_metrics(file_size, status_codes):
    """Prints accumulated metrics.
    Args:
        file_size (int): The total size of the read file so far.
        status_codes (dict): The count of each status code read so far.
    """
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                output_metrics(file_size, status_codes)
                line_count = 0

            line_count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if line[-2] in status_codes:
                        status_codes[line[-2]] += 1
                    else:
                        status_codes[line[-2]] = 1
            except IndexError:
                pass

        output_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        output_metrics(file_size, status_codes)
        raise
