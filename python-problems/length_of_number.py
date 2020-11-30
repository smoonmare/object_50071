#!/usr/bin/env python3

def number_length(x):
    string_number = ''
    i = 0

    string_number = str(x)
    for char in string_number:
        if char.isdigit():
            i += 1
    
    return i

print(number_length(-9999))