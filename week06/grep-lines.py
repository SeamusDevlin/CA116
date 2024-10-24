#!/usr/bin/env python3

import sys

pattern = sys.argv[1]

line = input().strip()
while line != 'end':
    if pattern in line:
        print(line)
    line = input().strip()
