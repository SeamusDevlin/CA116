#!/usr/bin/env python3

import sys

args = sys.argv[1]

with open(args, "w") as f:
   i = 2
   while i < len(sys.argv):
      s = sys.argv[i]
      f.write(s + "\n")
      i = i + 1
