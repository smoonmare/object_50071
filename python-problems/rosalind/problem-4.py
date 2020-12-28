#!/usr/bin/env python3

counter = 1
f_input = open('problem-4.txt', 'r')
text = f_input.readlines()
f_output = open('solution-4.txt', 'w')
for line in text:
    if counter % 2 == 0:
        print(line.strip())
        f_output.writelines(line)
    counter += 1