#!/usr/bin/env python3

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    s = files[i].split(".")
    if s[-1] == "py":
        print(files[i])
    i = i + 1
