'''
this script reads a .fasta file
argv[1] <-- .fastq
01/31/2017
Urmi
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

nA=0
nG=0
nC=0
nT=0
nAA=0
nGG=0
nAG=0
nGA=0
L1=0
L2=0
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid
	seq=str(record.seq)
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')
	#print seq
	#for each seq calculate #A #G #C #T and multiply
	nA=seq.count('A')
	nG=seq.count('G')
	nC=seq.count('C')
	nT=seq.count('T')
	
	pA=nA/len(seq)
	pG=nG/len(seq)
	pC=nC/len(seq)
	pT=nT/len(seq)
	#print pA,nA
	#print pG,nG
	#print pC,nC
	#print pT,nT
	#print pA+pG+pC+pT
	#print math.pow(pA,nA)
	L1=L1+(nA*math.log(pA))+(nG*math.log(pG))+(nC*math.log(pC))+(nT*math.log(pT))
	#print L1
	#break
	##calculate liklihood under alternate model
	##following params pA,pG,pC,pT,pGG,pGA,pAG,pAA
	nA=0
	nG=0
	nC=0
	nT=0
	nAA=0
	nGG=0
	nAG=0
	nGA=0
	total=0
	i=0
	tempseq=''
	while i < (len(seq)):
		#print i
		if i+1<len(seq):
			if seq[i]=='G' and seq[i+1]=='G':
				tempseq+='X'
				i=i+2
			elif seq[i]=='G' and seq[i+1]=='A':
				tempseq+='Y'
				i=i+2
			elif seq[i]=='G' and seq[i+1]=='T':
				tempseq+='G'
				i=i+1
			elif seq[i]=='G' and seq[i+1]=='C':
				tempseq+='G'
				i=i+1
			elif seq[i]=='A' and seq[i+1]=='A':
				tempseq+='A'
				i=i+1	
			elif seq[i]=='A' and seq[i+1]=='G':
				tempseq+='A'
				i=i+1
			elif seq[i]=='A' and seq[i+1]=='C':
				tempseq+='A'
				i=i+1
			elif seq[i]=='A' and seq[i+1]=='T':
				tempseq+='A'
				i=i+1
			elif seq[i]=='C':
				tempseq+='C'
				i=i+1
			elif seq[i]=='T':
				tempseq+='T'
				i=i+1	
		else:
			tempseq+=seq[i]
			i=i+1

	#print tempseq
	nA=tempseq.count('A')
	nG=tempseq.count('G')
	nC=tempseq.count('C')
	nT=tempseq.count('T')
	#nAA=tempseq.count('Z')
	#nAG=tempseq.count('W')
	nGG=tempseq.count('X')
	nGA=tempseq.count('Y')
	pA=nA/len(tempseq)
	pG=nG/len(tempseq)
	pC=nC/len(tempseq)
	pT=nT/len(tempseq)
	#pAA=nAA/len(tempseq)
	#pAG=nAG/len(tempseq)
	pGG=nGG/len(tempseq)
	pGA=nGA/len(tempseq)
	#print nGG,nAA,nAG,nGA,nA,nG,nC,nT,len(tempseq)
	print nGG,nGA,nA,nG,nC,nT,len(tempseq)
	L2=L2+(nA*math.log(pA))+(nG*math.log(pG))+(nC*math.log(pC))+(nT*math.log(pT))+(nGA*math.log(pGA))+(nGG*math.log(pGG))
		
	#break
print L1,L2,L1-L2,-2*(L1-L2)
