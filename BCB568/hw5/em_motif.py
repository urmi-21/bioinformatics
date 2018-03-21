'''
this is the EM algorithm for motif finding
INCOMPLETE
-Urmi
'''
from __future__ import division
import sys
import math


X=['GCTGTAG']
W=3

#initialize P, first column is the iid prob martix is rowwise
A=['A','C','G','T']
P=[[0.25,0.1,0.5,0.2],[0.25,0.4,0.2,0.1],[0.25,0.3,0.1,0.6],[0.25,0.2,0.2,0.1]]
#initialize Z uniform
Z=[[0.2,0.2,0.2,0.2,0.2]]


#start EM algorithm

#step 1 estimate Z from P
for i in range(len(X)):
	seq=X[i]
	print seq
	z_list=[]
	for j in range(len(seq)-W+1):
		print j
		#calculate P(Zij)=P(Xi|Zij)
		p=1
		for k in range(0,j):
			#print 'b',k
			p*=P[A.index(seq[k])][0]
			#print P[A.index(seq[k])][0],
		for k in range(j,j+W):
			#print 'm',k,k-j+1
			p*=P[A.index(seq[k])][k-j+1]	
			#print P[A.index(seq[k])][k-j+1],
		for k in range(j+W,len(seq)):
			#print 'b',k
			p*=P[A.index(seq[k])][0]
			#print P[A.index(seq[k])][0]
		print p
		z_list.append(p)
	s=sum(z_list)
	print s
	for j in range(len(z_list)):
		
		Z[i][j]=z_list[j]/s
	print Z[i],sum(Z[i])

#step 2 estimate P given Z

	
