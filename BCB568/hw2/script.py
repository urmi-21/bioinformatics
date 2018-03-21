'''
this script reads a .fastq file
argv[1] <-- .fastq
01/31/2017
Urmi
'''
from __future__ import division
import sys
from random import randint
import random
def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

with open(sys.argv[1]) as f:
    data=f.readlines()

#get the 802nd seq
ind=4*801
#print data[ind]
seq=data[ind+1].split('\n')[0]
#print seq
#seq='AAAGC'
#ans 1c
#define N
N=1000

#we have homopolymer GGGGGGGG of len 8
#we will calculate the prob of observing runs of len 8 or less if the null is runs are unusual
###########################
x=8	#the length of test statistic if x=8 we test if GGGGGGGG is unusual under the null
###########################
##################Method  for permutations####################################
#seq='AAGC'

all_rand=[]

for i in range(N):
	seq_copy=seq
	temp=''
	while len(temp)<len(seq):
		#generate a rand num for index of seq
		#sampling without replacement
		k=randint(0,len(seq_copy)-1)
		#print k
		temp=temp+seq_copy[k]
		#remove that base from seq
		seq_copy=seq_copy[0:k]+seq_copy[k+1:]
	all_rand.append(temp)
all_rand=list(set(all_rand))

#print all_rand

lens=[]
count=[]
tosearch=''
total=0
for i in range(len(seq)):
	total=0
	tosearch=tosearch+'G'
	for s in all_rand:
		total=total+occurrences(s, tosearch)
	count.append(total)	
	lens.append(len(tosearch))
#for i in range(len(lens)):
#	print str(lens[i])+"\t"+str(count[i])
count_x_ormore=sum(count[x-1:])
#print count_x_ormore,sum(count)
print 'Monte carlo: for length '+str(x)+', pval:',count_x_ormore/sum(count)
###########################################################################
#################1d, Bootstrap method######################################
#seq='AAGCT'
all_b_rand=[]
temp=''

for i in range(N):
	temp=''
	while len(temp)<len(seq):
		#generate a rand num for index of seq
		#sampling with replacement
		k=randint(0,len(seq)-1)
		#print k
		temp=temp+seq[k]
	all_b_rand.append(temp)
all_b_rand=list(set(all_b_rand))
#count the occ of diff lens og G
lens_b=[]
count_b=[]
##search the distribution of runs
tosearch=''
total=0
for i in range(len(seq)):
	total=0
	tosearch=tosearch+'G'
	for s in all_b_rand:
		total=total+occurrences(s, tosearch)
	count_b.append(total)	
	lens_b.append(len(tosearch))
#for i in range(len(lens_b)):
#	print str(lens_b[i])+"\t"+str(count_b[i])
count_x_ormore=sum(count_b[x-1:])
#print count_x_ormore,sum(count_b)
print 'Bootstrap: for length '+str(x)+', pval:',count_x_ormore/sum(count_b)
#print len(all_rand),len(all_b_rand)
#print len(seq),seq.count('A'),seq.count('C'),seq.count('G'),seq.count('T')


########################given parameters simulate data########################
pA=47/203
pG=51/203
pC=64/203
pT=41/203
all_g=[]
#print pA,pG,pC,pT
#print pA+pG+pC+pT
#generate N seq using the params
#seq='AAAAGCA'
#N=5
temp=''
for i in range(N):
	temp=''
	while len(temp)<len(seq):
		k=random.random()
		if k>=0 and k<pA:
			temp=temp+'A'
		elif k>=pA and k<pA+pG:
			temp=temp+'G'
		elif k>=pA+pG and k<pA+pG+pC:
			temp=temp+'C'
		else:
			temp=temp+'T'
	all_g.append(temp)

all_g=list(set(all_g))	

#count the occ of diff lens og G
lens_b=[]
count_b=[]
##search the distribution of runs
tosearch=''
total=0
for i in range(len(seq)):
	total=0
	tosearch=tosearch+'G'
	for s in all_g:
		total=total+occurrences(s, tosearch)
	count_b.append(total)	
	lens_b.append(len(tosearch))
#for i in range(len(lens_b)):
#	print str(lens_b[i])+"\t"+str(count_b[i])
count_x_ormore=sum(count_b[x-1:])
#print count_x_ormore,sum(count_b)
print 'Max likelihood: for length '+str(x)+', pval:',count_x_ormore/sum(count_b)




############################################part2: estimation of whole data set#######################################
seq_set=[]
for l in range(0,len(data),4):
	seq_set.append(data[l+1].split('\n')[0])

#print seq_set
D=''.join(seq_set)
L=len(D)
pA=D.count('A')/L
pG=D.count('G')/L
pC=D.count('C')/L
pT=D.count('T')/L
print "Max. Lik. Params for whole dataset pA pG pC pT"
print pA,pG,pC,pT
#print pA+pG+pC+pT

new_D=[]
N=100
#seq_set=['AACA','ACT','A']
###########generate dataset of same size#########

for s in seq_set:
	for i in range(N):
		temp=''
		while len(temp)<len(s):
			k=random.random()
			if k>=0 and k<pA:
				temp=temp+'A'
			elif k>=pA and k<pA+pG:
				temp=temp+'G'
			elif k>=pA+pG and k<pA+pG+pC:
				temp=temp+'C'
			else:
				temp=temp+'T'
		new_D.append(temp)

#print len(new_D)

####count runs of homopolymers in the null model new_D
# count runs of of length till 20
count_A=[]
count_G=[]
count_C=[]
count_T=[]
count_D=[[],[],[],[]]
tosearch=''
total=0
#new_D=['AAAGGGCCTTT']
A=['A','G','C','T']
for j in range (len(A)):
	tosearch=''
	for i in range(20):
		total=0
		tosearch=tosearch+A[j]
		for s in new_D:
			total=total+occurrences(s, tosearch)
		count_D[j].append(total)	
#print len(count_D[1])
		
#print the dist of homopolymers

#for j in range(len(count_D[0])):
#	s=count_D[0][j]+count_D[1][j]+count_D[2][j]+count_D[3][j]
#	print j+1,s
##finally calculate p value for len=8
count_x_ormore=sum(count_D[0][x-1:])+sum(count_D[1][x-1:])+sum(count_D[2][x-1:])+sum(count_D[3][x-1:])
total_sum=sum(count_D[0][:])+sum(count_D[1][:])+sum(count_D[2][:])+sum(count_D[3][:])
#print count_x_ormore,total_sum
print 'Whole dataset: for length '+str(x)+', pval:',count_x_ormore/total_sum

