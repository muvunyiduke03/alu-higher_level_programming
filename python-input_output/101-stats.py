#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
- Total file size
- Count of status codes in ascending order
"""


import sys


def print_stats(total_size, status_counts):
    """
    Prints the current statistics.

    Args:
        total_size (int): Total size of files processed.
        status_counts (dict): Dictionary with status code counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                file_size = int(parts[-1])
                total_size += file_size

                status_code = parts[-2]
                if status_code in valid_codes:
                    if status_code not in status_counts:
                        status_counts[status_code] = 0
                    status_counts[status_code] += 1
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)
