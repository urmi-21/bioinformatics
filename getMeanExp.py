import sys

#get mean exp of all transcripts
#phyloAll=[]
#define cols to skip
_C=16
with open(sys.argv[1]) as f:
	next(f)
	for l in f:
		temp=l.split('\n')[0].split(',')
		thisphylo=temp[1]
		if thisphylo == 'NA':
			continue
		thisTid=temp[0]
		totalexp=0
		for e in temp[_C:]:
			totalexp=totalexp+float(e)
		avg=totalexp/len(temp[_C:])
		print thisTid+'\t'+thisphylo+'\t'+str(avg)
		
