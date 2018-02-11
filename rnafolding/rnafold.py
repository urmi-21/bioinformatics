import sys, getopt
import os
from Bio import SeqIO
from Bio import SeqRecord
from Bio import Seq
from Bio import Alphabet

winsize=150
step=50


f=open("temp3.fa","w")
index=0
#open Sequence file
for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	#calculate composition
	length=len(record)	
	print seqid,length
	#print record.seq
	#create windows and calculate free energy
	for i in range(0,length-winsize+1,step):
		if i+step>length:
			print 'errrrrrrrrrrrr'
			break
		print ".",
		
		#filter all seqs with NNNNN		
			
		#save all seqs to file
		flag=False
		for x in record.seq[i:i+winsize]:
			if x=='N':
				flag=True
				break
		
		if(flag==False):
			f.write(">"+str(index)+"_"+str(i)+"..."+str(i+winsize)+"\n")
			f.write(str(record.seq[i:i+winsize]))		
			f.write("\n")
			index=index+1

		#create record
		
		#call RNAfold
		
#read temp file and calculate RNA fold
#for record in SeqIO.parse("temp.fa", "fasta"):
#	seqid=record.id
	#calculate composition
	#length=len(record)	
	#print seqid,length
	#call

#call rnafold
#os.system("RNAfold -i temp.fa -o rnaout")
