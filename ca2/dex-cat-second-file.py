#!/usr/bin/env python3

import sys

args = sys.argv[1:]

with open(sys.argv[1]) as f:
    a = f.read()

with open(a) as f:
    b = f.read()

sys.stdout.write(b)
