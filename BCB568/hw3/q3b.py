'''
this script reads a .fasta file
argv[1] <-- .fastq
01/31/2017
Urmi
'''
from __future__ import division
import sys
import math

#estimate markov chain o1 from whole dataset

#read subtype info from .txt file
with open(sys.argv[1],'r') as f:
	n= f.readlines()
with open(sys.argv[2],'r') as f:
	h= f.readlines()
sub_n=[0,0,0,0,0]
sub_h=[0,0,0,0,0]

for l in n:
	subtype=l.split('\t')[0]
	#print subtype

	if subtype=='Subtype_A':
		sub_n[0]+=1
	elif subtype=='Subtype_B':
		sub_n[1]+=1
	elif subtype=='Subtype_C':
		sub_n[2]+=1
	elif subtype=='Subtype_D':
		sub_n[3]+=1
	elif subtype=='CRF01_AE':
		sub_n[4]+=1

print sub_n
for l in h:
	subtype=l.split('\t')[1].split('\n')[0]
	#print subtype

	if subtype=='A':
		sub_h[0]+=1
	elif subtype=='B':
		sub_h[1]+=1
	elif subtype=='C':
		sub_h[2]+=1
	elif subtype=='D':
		sub_h[3]+=1
	elif subtype=='CRF01_AE':
		sub_h[4]+=1
print sub_h
