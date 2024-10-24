#!/usr/bin/env python3

import sys

punctuation_chars = list('. ,?!')
lines = sys.stdin.read().strip()
total_count = sum(1 for char in lines if char in punctuation_chars)

print(total_count)
