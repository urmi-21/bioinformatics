#!/usr/bin/env python
'''
this script reads a .coords and converts into .syn
synder readable format.
argv[1] <-- .coords
argv[2] <-- outfilename (.syn is appended)
argv[3] <-- option [F,S] (if F is given then use Fagin format in which refids are before query ids)
The inpur coords file has following columns
[S1] start of the alignment region in the reference sequence
[E1] end of the alignment region in the reference sequence
[S2] start of the alignment region in the query sequence 
[E2] end of the alignment region in the query sequence
{LEN 1] length of the alignment region in the reference sequence 
[LEN 2] length of the alignment region in the query sequence 
[% IDY] percent identity of the alignment 
[Tags] Ref and query fasta ids (in context of synder refrence is the focal species)

e.g.
    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
    1359     1476  |     1929     1813  |      118      117  |    94.92  | Chr1 BASO01015870.1
    1378     1476  |     1184     1281  |       99       98  |    94.95  | Chr1 BASO01017487.1


01/26/2017
Urmi
'''

import sys
import re

option=sys.argv[3]
strand='+'
#open file to write
fw=open(sys.argv[2]+".syn","w")
print sys.argv[1].split('.coords')[0]+".syn"

#OPEN .coords file
##Read the input file
l_index=0
with open(sys.argv[1]) as f:
    for l in f:
	#skip the headers
	if l_index<5:
		l_index=l_index+1
		continue
	vec=l.split()
	#print vec
	'''
	if(int(vec[11])==1):
		strand='+'
	else:
		strand='-'
	'''
		#break
	#print vec[-1]+"\t"+vec[3]+"\t"+vec[4]+"\t"+vec[-2]+"\t"+vec[0]+"\t"+vec[1]+"\t"+vec[9]+"\t"+strand
	'''
	vec[-1] will be the query seq id
	vec[-2] will be the reference seq id i.e. focal species id
	vec[0] and vec[1] is the start and end of alignment in reference sequence
	vec[3] and vec[4] is the start and end of alignment in query sequence
	NOTE: When the strand is negative the start and end query seq gets reversed as synder takes this information via the strand coloumn and the start should be less than end.

	-UrMi
	'''
	if int(vec[1]) <= int(vec[0]):
		print 'EROOOOOOORRRRRRRRRR'
		break
	if int(vec[3]) <= int(vec[4]):
		strand='+'
		if option=='F':
			fw.write(vec[-2]+"\t"+vec[0]+"\t"+vec[1]+"\t"+vec[-1]+"\t"+vec[3]+"\t"+vec[4]+"\t"+vec[9]+"\t"+strand+"\n")
		else:
			fw.write(vec[-1]+"\t"+vec[3]+"\t"+vec[4]+"\t"+vec[-2]+"\t"+vec[0]+"\t"+vec[1]+"\t"+vec[9]+"\t"+strand+"\n")
	else:	
		strand='-'
		if option == 'F':
			fw.write(vec[-2]+"\t"+vec[0]+"\t"+vec[1]+"\t"+vec[-1]+"\t"+vec[4]+"\t"+vec[3]+"\t"+vec[9]+"\t"+strand+"\n")		
		else:
			fw.write(vec[-1]+"\t"+vec[4]+"\t"+vec[3]+"\t"+vec[-2]+"\t"+vec[0]+"\t"+vec[1]+"\t"+vec[9]+"\t"+strand+"\n")




