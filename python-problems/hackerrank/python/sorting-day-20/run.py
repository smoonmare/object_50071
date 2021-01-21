#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_num = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swap_num += 1
    if swap_num == 0:
        break

print('Array is sorted in ' + str(swap_num) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[len(a)-1]))