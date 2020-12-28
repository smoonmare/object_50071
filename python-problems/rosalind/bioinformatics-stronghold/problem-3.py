#!/usr/bin/env python3
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def reverse_complement(seq):    
    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    return bases

with open('problem-3.txt', 'r') as f_input:
    dna = f_input.read().replace('\n', '')
dna_reverse = reverse_complement(dna)
with open('solution-3.txt', 'w') as f_output:
    f_output.writelines(dna_reverse)