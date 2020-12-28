#!/usr/bin/env python3
with open('problem-2.txt', 'r') as f_input:
    dna = f_input.read().replace('\n', '')
rna = dna.replace('T', 'U')
with open('solution-2.txt', 'w') as f_output:
    f_output.writelines(rna)