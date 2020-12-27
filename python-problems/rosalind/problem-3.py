#!/usr/bin/env python3
print("Input A and B")
a = int(input("A: "))
b = int(input("B: "))
sum = 0
for n in range(a,b+1):
    if n % 2 == 1:
        sum += n
print(f'The sum of all odd integers from {a} through {b}, inclusively, is {sum}')