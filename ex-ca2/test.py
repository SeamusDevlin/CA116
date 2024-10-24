#!/usr/bin/env python3

s = input()
dic = {}

i = 0
while i < len(s):
    if s not in dic:
        dic[s] = "true"
    i = i + 1

print(dic)
