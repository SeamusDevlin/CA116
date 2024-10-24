#!/usr/bin/env python3

month = int(input())
day = int(input())

day_of_year = (month - 1) * 30 + day

print((day_of_year - 1) % 7 + 1)
