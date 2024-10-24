#!/usr/bin/env python3

import sys

tasks = {}
name = sys.stdin.read().split()
count = 0

i = 0
while i < len(name):
    a = name[i].split(".")
    word = ".".join(a[:2])
    if a[2] == "correct":
        tasks[word] = 1
    elif a[2] == "incorrect":
        tasks[word] = 0
    i = i + 1

for key in tasks:
    if tasks[key] == 1:
        a = key.split(".")
        print(".".join(a[:2]))
