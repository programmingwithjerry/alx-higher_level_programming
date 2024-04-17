#!/usr/bin/python3
"""Reads from standard input line by line and computes metrics"""


def compute_metrics_and_print(size_total, status_code_counts):
    """Compute and print metrics statistics"""
    print("Total File Size: {}".format(size_total))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_code_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                compute_metrics_and_print(total_size, status_code_counts)
                line_count = 1
            else:
                line_count += 1

            line_parts = line.split()

            try:
                total_size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_parts[-2] in valid_codes:
                    if status_code_counts.get(line_parts[-2], -1) == -1:
                        status_code_counts[line_parts[-2]] = 1
                    else:
                        status_code_counts[line_parts[-2]] += 1
            except IndexError:
                pass

        compute_metrics_and_print(total_size, status_code_counts)

    except KeyboardInterrupt:
        compute_metrics_and_print(total_size, status_code_counts)
        raise

