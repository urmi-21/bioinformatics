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

#estimate markov chain o1 from whole dataset
p_whole=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
total=0
meanlen=0
totalseq=0
sun_ind=0
subtype=''
####Estimate markov chains for different subtypes####
#use list for diff subtypes e.g. p_subA=pAA,pAG,...,pTT
#      A  B  C  D  AE
p_sub=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#read subtype info from .txt file
with open(sys.argv[2],'r') as f:
	d= f.readlines()
#print d
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid.split('.')[0]
	seq=str(record.seq)
	
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')
	meanlen+=len(seq)
	#print len(seq)
	totalseq+=1
	#find the sub type
	for l in d:
		if seqid.split('.')[0] in l.split('\t')[-1].split('\n')[0]:
			subtype=l.split('\t')[0]

	if subtype=='Subtype_A':
		sub_ind=0
	elif subtype=='Subtype_B':
		sub_ind=1
	elif subtype=='Subtype_C':
		sub_ind=2
	elif subtype=='Subtype_D':
		sub_ind=3
	elif subtype=='CRF01_AE':
		sub_ind=4
	#print subtype,seqid, sub_ind
	for i in range(len(seq)-1):
		if seq[i]=='A' and seq[i+1]=='A':
			p_whole[0]+=1
			p_sub[sub_ind][0]+=1	
		elif seq[i]=='A' and seq[i+1]=='G':
			p_whole[1]+=1
			p_sub[sub_ind][1]+=1	
		elif seq[i]=='A' and seq[i+1]=='C':
			p_whole[2]+=1
			p_sub[sub_ind][2]+=1
		elif seq[i]=='A' and seq[i+1]=='T':
			p_whole[3]+=1
			p_sub[sub_ind][3]+=1
		elif seq[i]=='G' and seq[i+1]=='A':
			p_whole[4]+=1
			p_sub[sub_ind][4]+=1
		elif seq[i]=='G' and seq[i+1]=='G':
			p_whole[5]+=1	
			p_sub[sub_ind][5]+=1
		elif seq[i]=='G' and seq[i+1]=='C':
			p_whole[6]+=1
			p_sub[sub_ind][6]+=1
		elif seq[i]=='G' and seq[i+1]=='T':
			p_whole[7]+=1	
			p_sub[sub_ind][7]+=1
		elif seq[i]=='C' and seq[i+1]=='A':
			p_whole[8]+=1
			p_sub[sub_ind][8]+=1	
		elif seq[i]=='C' and seq[i+1]=='G':
			p_whole[9]+=1	
			p_sub[sub_ind][9]+=1
		elif seq[i]=='C' and seq[i+1]=='C':
			p_whole[10]+=1	
			p_sub[sub_ind][10]+=1
		elif seq[i]=='C' and seq[i+1]=='T':
			p_whole[11]+=1
			p_sub[sub_ind][11]+=1
		elif seq[i]=='T' and seq[i+1]=='A':
			p_whole[12]+=1	
			p_sub[sub_ind][12]+=1
		elif seq[i]=='T' and seq[i+1]=='G':
			p_whole[13]+=1	
			p_sub[sub_ind][13]+=1
		elif seq[i]=='T' and seq[i+1]=='C':
			p_whole[14]+=1	
			p_sub[sub_ind][14]+=1
		elif seq[i]=='T' and seq[i+1]=='T':
			p_whole[15]+=1
			p_sub[sub_ind][15]+=1

s=0
for i in range(0,16,4):
	#print i
	s=sum(p_whole[i:i+4])
	for k in range(i,i+4):
		#print k
		p_whole[k]=p_whole[k]/s
	print p_whole[i:i+4],sum(p_whole[i:i+4])
print '\n\n'
st=['A','B','C','D','AE']
for ind in range (5):	
	print 'Subtype_'+st[ind]
	for i in range(0,16,4):
		#print i
		s=sum(p_sub[ind][i:i+4])
		for k in range(i,i+4):
			#print k
			p_sub[ind][k]=p_sub[ind][k]/s
		print p_sub[ind][i:i+4],sum(p_sub[ind][i:i+4])
	print '\n\n'

##calculate lliklihood using whole data
L_whole=0
#liklihood A,B,C,D,AE
L_sub=[0,0,0,0,0]
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid.split('.')[0]
	seq=str(record.seq)
	
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')
#find the sub type
	for l in d:
		if seqid.split('.')[0] in l.split('\t')[-1].split('\n')[0]:
			subtype=l.split('\t')[0]

	if subtype=='Subtype_A':
		sub_ind=0
	elif subtype=='Subtype_B':
		sub_ind=1
	elif subtype=='Subtype_C':
		sub_ind=2
	elif subtype=='Subtype_D':
		sub_ind=3
	elif subtype=='CRF01_AE':
		sub_ind=4
	
	for i in range(len(seq)-1):
	
		if seq[i]=='A' and seq[i+1]=='A':
			L_whole+=math.log(p_whole[0])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][0])
	
		elif seq[i]=='A' and seq[i+1]=='G':
			L_whole+=math.log(p_whole[1])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][1])
		elif seq[i]=='A' and seq[i+1]=='C':
			L_whole+=math.log(p_whole[2])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][2])
		elif seq[i]=='A' and seq[i+1]=='T':
			L_whole+=math.log(p_whole[3])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][3])
		elif seq[i]=='G' and seq[i+1]=='A':
			L_whole+=math.log(p_whole[4])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][4])
		elif seq[i]=='G' and seq[i+1]=='G':
			L_whole+=math.log(p_whole[5])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][5])
		elif seq[i]=='G' and seq[i+1]=='C':
			L_whole+=math.log(p_whole[6])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][6])
		elif seq[i]=='G' and seq[i+1]=='T':
			L_whole+=math.log(p_whole[7])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][7])
		elif seq[i]=='C' and seq[i+1]=='A':
			L_whole+=math.log(p_whole[8])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][8])
		elif seq[i]=='C' and seq[i+1]=='G':
			L_whole+=math.log(p_whole[9])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][9])
		elif seq[i]=='C' and seq[i+1]=='C':
			L_whole+=math.log(p_whole[10])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][10])
		elif seq[i]=='C' and seq[i+1]=='T':
			L_whole+=math.log(p_whole[11])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][11])
		elif seq[i]=='T' and seq[i+1]=='A':
			L_whole+=math.log(p_whole[12])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][12])
		elif seq[i]=='T' and seq[i+1]=='G':
			L_whole+=math.log(p_whole[13])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][13])
		elif seq[i]=='T' and seq[i+1]=='C':
			L_whole+=math.log(p_whole[14])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][14])
		elif seq[i]=='T' and seq[i+1]=='T':
			L_whole+=math.log(p_whole[15])
			L_sub[sub_ind]+=math.log(p_sub[sub_ind][15])

	
print L_whole
print L_sub
print -2*(L_whole-sum(L_sub))




