#calculate zscore by random simulation

import sys, getopt
import os
from Bio import SeqIO
from Bio import SeqRecord
from Bio import Seq
from Bio import Alphabet
import subprocess
import random
import math

def average(s): return sum(s) * 1.0 / len(s)

N=100
zscores=[]
g=[]
for record in SeqIO.parse(sys.argv[1], "fasta"):
	delG=[]	
	seqid=record.id
	#calculate composition
	length=len(record)	
	print seqid,length
	#write this seq to a temp file to use
	f=open("z_temp.fa","w")
	f.write(">"+"temp\n")
	f.write(str(record.seq[0:length]))		
	f.close()
	#calculate original G
	output=subprocess.check_output("RNAfold --noPS -i z_temp.fa", shell=True)
	#print output.split('\n')[2].split(" ")[-1].split(")")[0]
	#get free energy from output
	delG.append(float(output.split('\n')[2].rsplit('(',1)[-1].split(")")[0]))
	g.append(float(output.split('\n')[2].rsplit('(',1)[-1].split(")")[0]))
	#print g
	
	#now make randomize seq and calculate delG
	temp_seq=record.seq[0:length]
	s='ABC123'
	for i in range(N):
		newseq = ''.join(random.sample(temp_seq,len(temp_seq)))
		#print newseq
		#write this seq to a temp file to use
		f=open("z_temp.fa","w")
		f.write(">"+"temp\n")
		f.write(str(newseq[0:length]))		
		f.close()
		#calculate original G
		output=subprocess.check_output("RNAfold --noPS -i z_temp.fa", shell=True)
		#get free energy from output
		#print output.split('\n')[2].rsplit('(',1)[-1].split(")")[0]
		delG.append(float(output.split('\n')[2].rsplit('(',1)[-1].split(")")[0]))
		
	#calculate the Z score based on all delG
	#get std dev of all delG
	all_avg=average(delG)
	rand_avg=average(delG[1:])
	var = map(lambda x: (x - all_avg)**2, delG)
	sigma=math.sqrt(average(var))
	print 'sigma=',sigma
	print 'all avg=',all_avg
	print 'rand_avg=',rand_avg
	if sigma==0:
		print 'sigma=0',seqid
		zscores.append(0)
	else:
		thisz=(delG[0]-rand_avg)/sigma
		zscores.append(thisz)
print delG
print zscores
print g
'''
print zscores
#write Zscores to file
f=open("z_scores_temp3.txt","w")
for i in zscores:
	f.write(str(i)+"\n")		
f.close()

f=open("delG_scores_temp3.txt","w")
for i in g:
	print i
	f.write(str(i)+"\n")		
f.close()
'''

