'''
count line split bt delims
[1] file name
[2] delim index
urmi
'''
import sys

delims=['\t',',',' ',';']
i=int(sys.argv[2])
with open(sys.argv[1],'r') as f:
	data=f.read().splitlines()
num_headrs=[]
for d in data:
	#print len(d.split(delims[i]))
	if len(d.split(delims[i])) not in num_headrs:
		num_headrs.append(len(d.split(delims[i])))
print num_headrs
if len(num_headrs) > 1:
	print 'File is not consistent with given header'
