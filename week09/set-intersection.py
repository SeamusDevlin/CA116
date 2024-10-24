#!/usr/bin/env python3

with open("a.txt") as f:
    a = f.readlines()
with open("b.txt") as f:
    b = f.readlines()

animal = {}

i = 0
while i < len(a):
    if a[i] in b:
        animal[a[i]] = "true"
    i = i + 1

if animal != {}:
    print("".join(animal).rstrip())
