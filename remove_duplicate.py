'''
Read data file and remove duplicate
'''
import sys

tids=[]
#open file
with open(sys.argv[1],'r') as f:
	for l in f:
		#print l.split(',')[0].replace('"','')
		thisid=l.split(',')[0].replace('"','').split('.')[0]
		if not thisid in tids:
			tids.append(thisid)
		else:
			print thisid,'is repeated'
print len(tids)
print len(set(tids))
