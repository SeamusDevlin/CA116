#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    s = files[i].split(".")
    if s[-1] == "py":
        print(files[i])
    i = i + 1

i = 0
while i < len(files):
    with open(files[i]) as f:
        f.readline(0)
        if 
