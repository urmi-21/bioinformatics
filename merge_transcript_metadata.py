'''
This script merges transcript metadata into data file which will be read by metaomgraph.
the search column is specified in the script so change it if metadata file columns change.
Urmi
'''
import sys

#read metadata file
with open(sys.argv[1],'r') as f:
	metadata=f.read().splitlines()

#print metadata
data_delim=","
metadata_delim=","
tname=int(sys.argv[3])
ctr=0
#read data file
with open(sys.argv[2],'r') as f:
         for line in f:
		ctr+=1
		#print ctr
		sys.stderr.write(str(ctr)+"\n")
		temp=line.split(data_delim)	#data file delimiter here
		thisname=temp[0].split('.')[0].replace('"','')
		#find thisname in column x of metadata
		for m in metadata:
			m=m.replace('"','')
			temp2=m.split(metadata_delim)	#metadata delimiter here
			#print temp2[tname],thisname
			if temp2[tname]==thisname:
				newstr=data_delim.join(temp2)+data_delim+"".join(temp[1:])
				print newstr+"\n"
				break
