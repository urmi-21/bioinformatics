'''
This script reads a blast output in following format
-outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe'
Then it finds unique query target pair such that the corressponding evalue is mi for that query
Urmi
'''

import sys

qprotlist=[]
tprotlist=[]
min_eval=[]

with open(sys.argv[1],'r') as f:
	for l in f:
		temp=l.split('\t')
		thisqp=temp[0]
		thistp=temp[1]
		thiseval=float(temp[3])
		if thisqp not in qprotlist:
			qprotlist.append(thisqp)
			tprotlist.append(thistp)
			min_eval.append(thiseval)
		else:
			if thiseval < min_eval[-1]:
				min_eval[-1]=thiseval
				tprotlist[-1]=thistp

for i in range(len(qprotlist)):
	print qprotlist[i],tprotlist[i],min_eval[i]
