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
import random
from random import randint
from itertools import product

def score(M,PSM):
	s=1
	ls=0
	t=PSM[0][0]+PSM[1][0]+PSM[2][0]+PSM[3][0]
	for i in range(len( M )):
		if M[i]=='A':
			s=s*(PSM[0][i]/t)
			if (PSM[0][i]/t) > 0:
				ls+=math.log(PSM[0][i]/t)
			else:
				ls+=0		
		if M[i]=='C':
			s=s*(PSM[1][i]/t)
			if (PSM[1][i]/t) > 0:
				ls+=math.log(PSM[1][i]/t)
			else:
				ls+=0	
		if M[i]=='G':
			s=s*(PSM[2][i]/t)
			if (PSM[2][i]/t) > 0:
				ls+=math.log(PSM[2][i]/t)
			else:
				ls+=0	
		if M[i]=='T':
			s=s*(PSM[3][i]/t)
			if (PSM[3][i]/t) > 0:
				ls+=math.log(PSM[3][i]/t)
			else:
				ls+=0	
	return s
##given current state and transition prob matrix, generate next state
def nextstate(curr,tp):
	#generate a random int
	r=random.random()
	#there are only 4 possible transitions
	if r<=tp[0][curr]:
		return 0
	elif r>tp[0][curr] and r<=tp[0][curr]+tp[1][curr]:
		return 1
	elif r>tp[0][curr]+tp[1][curr] and r<=tp[0][curr]+tp[1][curr]+tp[2][curr]:
		return 2
	else:
		return 3
def getinitstate(isd,states):
	isd, states = (list(x) for x in zip(*sorted(zip(isd, states), key=lambda pair: pair[0])))
	#print isd[-6:]
	#print states[-6:]
	#choose randomly among top 10 mostlikily states
	return states[randint(len(states)-10,len(states)-1)]
	
	
motif1='GGCGCC'
PSM1=[[13,0, 0,  0,  3,  2],
      [0,  1, 65, 34, 96, 85],
      [85, 96, 34, 65,  1,  0],
      [2,  3,  0,  0,  0, 13]]

motif2='GGTCAAAGGT'
PSM2=[[0 , 0 , 0 , 2 ,41, 41 ,39 , 0 , 0,  0],
       [0 , 0 , 2, 37 , 0 , 0 , 0 , 0  ,0 , 2],
       [41 ,39 , 0 , 2,  0 , 0,  2 ,41, 39 , 0],
        [0  ,2, 39,  0,  0,  0,  0,  0,  2 ,39]]

maxs=-100
mseq=''
c=0

#print score('GGCGCC',PSM1)
#sys.exit()
'''
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid.split('.')[0]
	seq=str(record.seq)
	
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')

	#print seq
	for k in range(len(seq)-len(motif2)+1):

		#temp=seq[k:k+len(motif1)]
		temp=seq[k:k+len(motif2)]
		if score(temp,PSM2) > maxs:
			maxs=score(temp,PSM2)
			mseq=temp
		sc=score(temp,PSM2)
		print temp,sc			#plot these scores to see histogram
'''		

############These were empiracally chosen after looking at the distribution of likelihoods of all motifs
cutoff1=0.10
cutoff2=0.7
############################
#get all motifs which have score more than cutoffs
print 'Finding motifs with liklihood above cutoff...'
m1=[]
m2=[]
for record in SeqIO.parse(sys.argv[1], "fasta"):
	break
	seqid=record.id
	#print seqid.split('.')[0]
	seq=str(record.seq)
	
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')

	#print seq
	
	for k in range(len(seq)-len(motif1)+1):

		#temp=seq[k:k+len(motif1)]
		temp=seq[k:k+len(motif1)]
		if score(temp,PSM1) > maxs:
			maxs=score(temp,PSM1)
			mseq=temp
		sc=score(temp,PSM1)
		if sc > cutoff1:
			#print temp
			m1.append(temp)

	
	for k in range(len(seq)-len(motif2)+1):

		#temp=seq[k:k+len(motif1)]
		temp=seq[k:k+len(motif2)]
		if score(temp,PSM2) > maxs:
			maxs=score(temp,PSM2)
			mseq=temp
		sc=score(temp,PSM2)
		if sc > cutoff2:
			#print temp
			m2.append(temp)	
#print len(m1),len(m2)
m1=['GGCCCC', 'GGGGCC', 'GGCGCC']
m2=['GGTCAAAGGT']
m1=list(set(m1))
m2=list(set(m2))

print m1,m2
#print m2
###learn markov chain of order 3
o=2	##define order
states=[]
TPM=[[],[],[],[]]	#transition of all states to A,C,G or T
ISD=[]			#init state dist
Alphabet=['A','C','G','T']
for roll in product(Alphabet, repeat = o):
	states.append(''.join(roll))
#print states
##init TMP
for l in TPM:
	for x in range(len(states)):
		l.append(0)
for x in range(len(states)):
	ISD.append(0)
#print TPM
#seq='ACGATCA'
'''
for i in range(len(seq)-o):
		temp=seq[i:i+o]
		print temp,seq[i+o]
		##updates counts in TPM
		#search for index of temp
		print states.index(temp)
		print Alphabet.index(seq[i+o])
		TPM[Alphabet.index(seq[i+o])][states.index(temp)]+=1
'''


#sys.exit()
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid.split('.')[0]
	seq=str(record.seq)
	#print len(seq)
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')

	#print seq
	for i in range(len(seq)-o):
		
		temp=seq[i:i+o]
		#print temp,seq[i+o]
		##updates counts in TPM
		#search for index of temp
		#print states.index(temp)
		#print Alphabet.index(seq[i+o])
		TPM[Alphabet.index(seq[i+o])][states.index(temp)]+=1
		if(i==0):
			ISD[states.index(temp)]+=1


#convert TPM to a probability matrix
#print TPM
for x in range(len(states)):
		s=TPM[0][x]+TPM[1][x]+TPM[2][x]+TPM[3][x]
		TPM[0][x]=TPM[0][x]/s
		TPM[1][x]=TPM[1][x]/s
		TPM[2][x]=TPM[2][x]/s
		TPM[3][x]=TPM[3][x]/s
isd_sum=sum(ISD)
for x in range( len(ISD)):
	ISD[x]=ISD[x]/isd_sum
	
#print TPM
#print ISD,sum(ISD)

#simulate 1000 datasets with 2135 seqs from markov chain each of len 1000
print 'Simulating MC...'
N=500
D=[]
sim_data=[]

for s in range (N):
	sim_data=[]
	for n in range(2135):
		#print '.',
		temp=''
		#choose initial state randomly
		#temp+=states[randint(0,len(states)-1)]
		temp+=getinitstate(ISD,states)
		#print temp
		while len(temp)<1000:
			#print temp[-3:]
			curr=states.index(temp[-o:])
			temp+= Alphabet[nextstate(curr,TPM)]
			#print temp
		sim_data.append(temp)
	
	D.append(sim_data)

##test occurances and spacing of motifs
##
#Calculate test statistic
num_motif1=0
num_motif2=0
num_both=0
space=[]
#count total motifs in data
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#print seqid.split('.')[0]
	seq=str(record.seq)
	#print len(seq)
	#filter seq and remove char other that AGCT
	for x in seq:
		if x not in {'A','G','C','T'}:
			#print x
			seq=seq.replace(x,'')
	for x in m1:
		if x in seq:
			num_motif1+=1
	for x in m2:
		if x in seq:
			num_motif2+=1

	#check space if these motifs are there
	for x in m1:
		if x in seq:
			for y in m2:
				if y in seq:
					space.append(seq.index(x)-seq.index(y))
					num_both=+1
					
print 'Ts',num_motif1,num_motif2,space		

##test if motif 1 is represented by MC(3)
TS1=0	#test stat for motif1
TS2=0	#test stat for motif2
TS_both=0
TS3=[]
for d in D:
	c1=0
	c2=0
	c_both=0
	f=0
	f_ind=-1
	for x in d:
		for y in m1:
			if y in x:
				c1+=1 
				f=1
				f_ind=x.index(y)
		for y2 in m2:
			if y2 in x:
				c2+=1 
				if f_ind>=0:
					TS3.append(f_ind-x.index(y2))
					c_both+=1
	
	#print c1,c2
	if c1 >= num_motif1:
		TS1+=1
	if c2>= num_motif2:
		TS2+=1
	if c_both>= num_both:
		TS_both+=1
#print 'TS1','TS2','TS1/N','TS_both','TS_both/N','TS2/N'
#print TS1,TS2,TS1/N,TS2/N,TS_both,TS_both/N,TS3

print 'pvalue for motif1:',TS1/N
print 'pvalue for motif2:',TS2/N
print 'pvalue for both on single seq:',TS_both/N
