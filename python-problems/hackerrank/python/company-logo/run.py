#!/bin/python3
import collections

if __name__ == '__main__':
    s = input()
    s = sorted(s)
    counter_s = collections.Counter(s).most_common()
    counter_s = sorted(counter_s, key=lambda x: (x[1] * -1, x[0]))
    for i in range(0,3):
        print(counter_s[i][0], counter_s[i][1])