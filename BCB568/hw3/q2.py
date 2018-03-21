'''
this script reads a .fasta file
argv[1] <-- .fastq
01/31/2017
Urmi
'''
from __future__ import division
import sys
import math
from Bio import SeqIO
from Bio.Seq import Seq
from random import randint
import random

#estimate markov chain o1
pAA=0
pAG=0
pAC=0
pAT=0
pGA=0
pGG=0
pGC=0
pGT=0
pCA=0
pCG=0
pCC=0
pCT=0
pTA=0
pTG=0
pTC=0
pTT=0
tA=0
tG=0
tC=0
tT=0
cA=0
cG=0
cC=0
cT=0
total=0
lens=[]
totalseq=0
T=0		#test stat num of TGGG in orignal
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid
	seq=str(record.seq)
	
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')
	lens.append(len(seq))
	#print len(seq)
	#print seq.count('TGGG')
	T+=seq.count('TGGG')
	totalseq+=1
	if seq[0]=='A':
		cA+=1
	elif seq[0]=='G':
		cG+=1
	elif seq[0]=='C':
		cC+=1
	elif seq[0]=='T':
		cT+=1
	
	for i in range(len(seq)-1):
		if seq[i]=='A' and seq[i+1]=='A':
			pAA+=1
			tA+=1	
		elif seq[i]=='A' and seq[i+1]=='G':
			pAG+=1
			tA+=1	
		elif seq[i]=='A' and seq[i+1]=='C':
			pAC+=1	
			tA+=1
		elif seq[i]=='A' and seq[i+1]=='T':
			pAT+=1	
			tA+=1
		elif seq[i]=='G' and seq[i+1]=='A':
			pGA+=1	
			tG+=1
		elif seq[i]=='G' and seq[i+1]=='G':
			tG+=1
			pGG+=1	
		elif seq[i]=='G' and seq[i+1]=='C':
			tG+=1
			pGC+=1	
		elif seq[i]=='G' and seq[i+1]=='T':
			tG+=1
			pGT+=1	
		elif seq[i]=='C' and seq[i+1]=='A':
			tC+=1
			pCA+=1	
		elif seq[i]=='C' and seq[i+1]=='G':
			tC+=1
			pCG+=1	
		elif seq[i]=='C' and seq[i+1]=='C':
			tC+=1
			pCC+=1	
		elif seq[i]=='C' and seq[i+1]=='T':
			tC+=1
			pCT+=1	
		elif seq[i]=='T' and seq[i+1]=='A':
			tT+=1
			pTA+=1	
		elif seq[i]=='T' and seq[i+1]=='G':
			tT+=1
			pTG+=1	
		elif seq[i]=='T' and seq[i+1]=='C':
			tT+=1
			pTC+=1	
		elif seq[i]=='T' and seq[i+1]=='T':
			tT+=1
			pTT+=1	
		total+=1

pAA=pAA/tA
pAG=pAG/tA
pAC=pAC/tA
pAT=pAT/tA
pGA=pGA/tG
pGG=pGG/tG
pGC=pGC/tG
pGT=pGT/tG
pCA=pCA/tC
pCG=pCG/tC
pCC=pCC/tC
pCT=pCT/tC
pTA=pTA/tT
pTG=pTG/tT
pTC=pTC/tT
pTT=pTT/tT
cA=cA/totalseq
cG=cG/totalseq
cC=cC/totalseq
cT=cT/totalseq

print pAA,pAG,pAC,pAT,pAA+pAG+pAC+pAT
print pGA,pGG,pGC,pGT,pGA+pGG+pGC+pGT
print pCA,pCG,pCC,pCT, pCA+pCG+pCC+pCT
print pTA,pTG,pTC,pTT, pTA+pTG+pTC+pTT

print cA,cG,cC,cT
print 'Total Seq:',totalseq
###sys.exit()
#generate 10000 data sets
print 'Monte Carlo simulation......'
N=10
s1=0
chars=['A','G','C','T']
for x in range (N):
	seqs=[]
	for k in range(len(lens)):
		temp=''
		r1=random.random()
		if r1>=0 and r1<cA:
			temp=temp+'A'
		elif r1>=cA and r1<cA+cG:
			temp=temp+'G'
		elif r1>=cA+cG and r1<cA+cG+cC:
			temp=temp+'C'
		else:
			temp=temp+'T'
		#print temp
		
		temp=temp+chars[randint(0,3)] #random start nuc
		#print temp
		for i in range(lens[k]-1):
			curr=temp[-1]
			r=random.random()
			#print r
			if curr == 'A':
				if r>=0 and r<pAA:
					temp=temp+'A'
				elif r>=pAA and r<pAA+pAG:
					temp=temp+'G'
				elif r>=pAA+pGG and r<pAA+pAG+pAC:
					temp=temp+'C'
				else:
					temp=temp+'T'
	
	
			elif curr == 'G':
				if r>=0 and r<pGA:
					temp=temp+'A'
				elif r>=pGA and r<pGA+pGG:
					temp=temp+'G'
				elif r>=pGA+pGG and r<pGA+pGG+pGC:
					temp=temp+'C'
				else:
					temp=temp+'T'
	
			elif curr == 'C':
				if r>=0 and r<pCA:
					temp=temp+'A'
				elif r>=pCA and r<pCA+pCG:
					temp=temp+'G'
				elif r>=pCA+pCG and r<pCA+pCG+pCC:
					temp=temp+'C'
				else:
					temp=temp+'T'
	
			elif curr == 'T':
				if r>=0 and r<pTA:
					temp=temp+'A'
				elif r>=pTA and r<pTA+pTG:
					temp=temp+'G'
				elif r>=pTA+pTG and r<pTA+pTG+pTC:
					temp=temp+'C'
				else:
					temp=temp+'T'
	
		seqs.append(temp)
	#print (seqs)
	#count total TGGG present in each simulated dataset
	tot=0
	for s in seqs:
		#print s.count('TGGG')
		tot+=s.count('TGGG')		
	print tot
	if tot<=T:
		s1+=1	
print 'test S:',T,'pval:',s1/N
