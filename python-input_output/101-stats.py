#!/usr/bin/env python3
"""
Script that reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
        if a status code doesn’t appear, don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
"""

import sys

def print_statistics(total_size, status_counts):
    """
    Print statistics including total file size and number of lines by status code.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def process_input_line(line, total_size, status_counts):
    """
    Process a single line of input, update metrics, and return the updated values.

    Args:
        line (str): Input line in the specified format.
        total_size (int): Current total file size.
        status_counts (dict): Current counts of lines for each status code.

    Returns:
        tuple: Updated total file size and status code counts.
    """
    try:
        # Extract relevant information from the input line
        parts = line.split()
        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update total file size
        total_size += file_size

        # Update status code counts
        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        return total_size, status_counts

    except (ValueError, IndexError):
        # Ignore lines with incorrect format
        return total_size, status_counts

def main():
    """
    Main function to read input, compute metrics, and print statistics.
    """
    total_size = 0
    status_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            total_size, status_counts = process_input_line(line.strip(), total_size, status_counts)

            if line_number % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
