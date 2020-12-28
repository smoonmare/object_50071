#!/usr/bin/env python3
result = {}
with open('problem-1.txt', 'r') as file:
    dna = file.read().replace('\n', '')
for keys in dna:
    result[keys] = result.get(keys, 0) + 1
for i in sorted (result) :  
     print(result[i], end =" ")