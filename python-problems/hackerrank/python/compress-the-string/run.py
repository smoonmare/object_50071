from itertools import *

def compress_string(input_string):
    for key, group in groupby(input_string):
        yield len(tuple(group)), int(key)

s_input = input()
print(*compress_string(s_input))