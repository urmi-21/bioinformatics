'''
Keep only best hit from blast result (the fist hit by default)
'''
import sys
done=[]
with open(sys.argv[1]) as f:
	for l in f:
		thisId=l.split('\t')[0]
		if thisId in done:
			continue
		else:
			done.append(thisId)
			print l.split('\n')[0]
