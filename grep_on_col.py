'''
This file reads a file containg values and filters other file on a specified col with that value
[1]--> list of terms
[2]--> file
[3]--> col num
[4]--> print lines containing 1 or not containg 0
[5]--> delim 0-->tab,1-->comma,2-->semicolon,3-->space
Urmi
'''

import sys
col=int(sys.argv[3])
opt=int(sys.argv[4])
delimis=["\t",",",";"," "]
filedelim=delimis[int(sys.argv[5])]
print "delim is", filedelim
#open file 1
with open(sys.argv[1],'r') as f:
	tosearch=f.read().splitlines()
tosearch=set(tosearch)
#read file and print filtered lines
with open(sys.argv[2],'r') as f:
	for line in f:
		temp=line.split(filedelim)
		if opt == 1:
			print temp[col]
			if temp[col] in tosearch:
				print line
		if opt == 0:
			if temp[col] not in tosearch:
				print line

