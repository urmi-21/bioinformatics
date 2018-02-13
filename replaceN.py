#!/usr/bin/env python
'''
this script reads a fasta and replaces all lowercase to N
argv[1] <-- fastafile
01/27/2017
Urmi
'''

import sys
#read repeatmasker.out
f2=open(sys.argv[1].split('.fna')[0]+".masked.fna",'w')
print f2
with open(sys.argv[1], 'r') as f:
    for line in f:
	if '>' in line:
		f2.write(line)
	else :
		temp=line.replace('a','N')
		temp=temp.replace('g','N')
		temp=temp.replace('c','N')
		temp=temp.replace('t','N')
		f2.write(temp)   
