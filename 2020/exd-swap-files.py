#!/usr/bin/env python3

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as f1:
    content1 = f1.read()

with open(file2 , "r") as f2:
    content2 = f2.read()

with open(file1, "w") as f1:
    f1.write(content2)

with open(file2, "w") as f2:
    f2.write(content1)
