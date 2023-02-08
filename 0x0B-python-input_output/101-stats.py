#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


def print_metrics():
    """Each 10 lines and after a keyboard interruption,
    prints those statistics since the beginning:
    Total file size: File size: <total size>
    where is the sum of all previous
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}

    try:
        line_count = 0
        while True:
            line = input()
            line_count += 1
            elements = line.split()
            total_size += int(elements[-1])
            status_codes[int(elements[-2])] += 1

            if line_count % 10 == 0:
                print("Total file size: ", total_size)
                for status_code in sorted(status_codes.keys()):
                    if status_codes[status_code] > 0:
                        print("{}: {}".format(status_code,
                                              status_codes[status_code]))
    except KeyboardInterrupt:
        print("Total file size: ", total_size)
        for status_code in sorted(status_codes.keys()):
            if status_codes[status_code] > 0:
                print("{}: {}".format(status_code, status_codes[status_code]))


if __name__ == "__main__":
    print_metrics()
