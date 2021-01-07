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