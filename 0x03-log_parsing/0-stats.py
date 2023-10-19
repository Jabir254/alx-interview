#!/usr/bin/python3
"""A scripts that read stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict

# Regular expression pattern to match the input format
log_pattern = re.compile(r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

# Initialize variables
total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            ip, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Handle CTRL + C to print statistics and exit
    print("File size:", total_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
