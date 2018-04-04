import sys

#read phylo info in dict
t_p={}
with open(sys.argv[1]) as f:
	for l in f:
		temp=l.replace('"','').split('\n')[0].split(',')
		t_p[temp[0]]=temp[1]

print t_p["ENST00000618751"]

#open cpm file
f2=open("resfile.csv",'w')
firstline=True
i=0
with open(sys.argv[2],'r') as f:
	for l in f:
		print i
		if firstline:
			temp=l.split('\n')[0].split(',')
			f2.write(temp[0]+',Strata,'+','.join(temp[1:])+'\n')
			firstline=False
		else:		
			temp=l.split('\n')[0].split(',')
			this_tid=temp[0]
			if this_tid in t_p:
				this_phylo=t_p[this_tid]
				f2.write(temp[0]+','+this_phylo+','+','.join(temp[1:])+'\n')
			else:
				f2.write(temp[0]+','+'NA'+','+','.join(temp[1:])+'\n')
		i=i+1				
		
f2.close()
