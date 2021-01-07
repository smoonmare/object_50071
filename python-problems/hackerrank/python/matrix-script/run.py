#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
message = ''
decoded_message = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for column in range(m):
    for row in range(n):
        message += matrix[row][column]
decoded_message = re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', message)
print(decoded_message)
'''
Test string:
    This$#is% Matrix#  %!
Explanation:
\b[^a-zA-Z0-9]+\b / gm
--- \b assert position at a word boundary: (^\\w|\\w$|\\W\\w|\\w\\W)
    Match a single character not present in the list below [^a-zA-Z0-9]+
    -  + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
    -  a-z a single character in the range between a (index 97) and z (index 122) (case sensitive)
    -  A-Z a single character in the range between A (index 65) and Z (index 90) (case sensitive)
    -  0-9 a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
--- \b assert position at a word boundary: (^\\w|\\w$|\\W\\w|\\w\\W)
    Global pattern flags
    -  g modifier: global. All matches (don't return after first match)
    -  m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
Match information:
    Match 1: Full match 4-6: $#
    Match 2: Full match 8-10: %[space]
'''