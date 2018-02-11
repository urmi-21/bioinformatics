'''
extract fasta from a list
'''
from __future__ import division
import sys
import math
import re
from Bio import SeqIO
from Bio.Seq import Seq
import regex as re
import time
from random import randint

#open list file
with open(sys.argv[1],'r') as f:
	ids=f.readlines()
print ids
ids2=[]
for x in ids:
	ids2.append(x.split('\n')[0])

#open fasta
total=0
output_handle = open(sys.argv[3], "w")
for record in SeqIO.parse(sys.argv[2], "fasta"):
	
	seqid=record.id
	desc= record.description
	if seqid in ids2:
		SeqIO.write(record, output_handle, "fasta")
		total=total+1
