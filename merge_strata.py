import sys

#read prot_feat file
metazoa=["Eumetazoa","Bilateria","Deuterostomia","Chordata"]
euk=['Opisthokonta']
euteleostomi=["Sarcopterygii","Tetrapoda","Amniota"]
theria=["Eutheria","Boreoeutheria","Euarchontoglires"]
primates=["Haplorrhini","Simiiformes","Catarrhini","Hominoidea","Hominidae","Homininae"]

new=[]
with open(sys.argv[1]) as f:
	for l in f:
		temp=l.split('\n')[0].split('\t')
		if temp[-1] in euk:
			new.append('\t'.join(temp[:-1])+'\tEukaryota')
		elif temp[-1] in metazoa:
			new.append('\t'.join(temp[:-1])+'\tMetazoa')
		elif temp[-1] in euteleostomi:
			new.append('\t'.join(temp[:-1])+'\tEuteleostomi')
		elif temp[-1] in theria:
			new.append('\t'.join(temp[:-1])+'\tTheria')
		elif temp[-1] in primates:
			new.append('\t'.join(temp[:-1])+'\tPrimates')
		else:
			new.append('\t'.join(temp))

f=open('prot_combined_feats_merged.txt','w')
for s in new:
	f.write(s+'\n')
f.close()
