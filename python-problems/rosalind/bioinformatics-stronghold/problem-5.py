#!/usr/bin/env python3
import re

def gc_content(sequence):
    percentage = (sequence.count('C') + sequence.count('G')) / len(sequence) * 100
    return percentage

def main():
    with open('problem-5.txt', 'r') as f_input:
        data = f_input.read().replace('\n', '')
        

if __name__ == "__main__":
    main()