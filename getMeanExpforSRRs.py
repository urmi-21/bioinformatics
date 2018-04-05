import sys

#get mean exp of all transcripts
#phyloAll=[]
#define cols to skip
#enter the SRRs needed to get mean exp
#testis runs
#_SRR=['206980','206979','206981','206978','2040581','2040583','2040582']
#brain runs
#_SRR=["SRR835931","SRR835929","SRR835930","SRR903294","SRR903295","SRR903291","SRR903285","SRR903284","SRR903292","SRR903238","SRR903283","SRR903235","SRR903297","SRR903287","SRR903276","SRR903290","SRR903296","SRR903282","SRR903288","SRR903300","SRR903274","SRR903301","SRR903237","SRR903302","SRR903239","SRR903236","SRR903278","SRR903286","SRR903281","SRR903240","SRR903212","SRR903275","SRR903216","SRR903214","SRR903289","SRR903217","SRR903210","SRR903280","SRR903213","SRR903277","SRR903241","SRR903218","SRR903304","SRR903279","SRR903233","SRR903221","SRR903231","SRR903298","SRR903293","SRR903219","SRR903211","SRR903305","SRR903222","SRR903232","SRR903224","SRR903220","SRR903226","SRR903303","SRR903225","SRR903227","SRR903299","SRR903234","SRR903215","SRR903230","SRR903228","SRR903229","SRR903223","SRR2040575","SRR2040576"]
#Huntington disease runs
#_SRR=["SRR1747161","SRR1747160","SRR1747170","SRR1747163","SRR1747186","SRR1747188","SRR1747150","SRR1747162","SRR1747191","SRR1747190","SRR1747147","SRR1747211","SRR1747172","SRR1747189","SRR1747165","SRR1747194","SRR1747167","SRR1747175","SRR1747164","SRR1747174","SRR1747153","SRR1747158","SRR1747203","SRR1747169","SRR1747207","SRR1747209","SRR1747145","SRR1747146","SRR1747199","SRR1747143","SRR1747166","SRR1747192","SRR1747197","SRR1747179","SRR1747156","SRR1747193","SRR1747176","SRR1747196","SRR1747173","SRR1747182","SRR1747202","SRR1747181","SRR1747201","SRR1747208","SRR1747144","SRR1747149","SRR1747204","SRR1747185","SRR1747168","SRR1747205","SRR1747200","SRR1747157","SRR1747184","SRR1747171","SRR1747159","SRR1747180","SRR1747154","SRR1747210","SRR1747195","SRR1747177","SRR1747152","SRR1747198","SRR1747183","SRR1747178","SRR1747155","SRR1747148","SRR1747151","SRR1747206","SRR1747187","SRR2121907","SRR2121909","SRR2121908"]
#breast cancer runs
_SRR=["SRR2532354","SRR2532321","SRR2532322","SRR2532316","SRR2532315","SRR2532323","SRR2532319","SRR2532363","SRR2532355","SRR2532367","SRR2532327","SRR2532353","SRR2532356","SRR2532329","SRR2532352","SRR2532349","SRR2532365","SRR2532325","SRR2532364","SRR2532357","SRR2532361","SRR2532317","SRR2532393","SRR2532328","SRR2532330","SRR2532358","SRR2532320","SRR2532380","SRR2532331","SRR2532396","SRR2532387","SRR2532372","SRR2532389","SRR2532388","SRR2532368","SRR2532346","SRR2532360","SRR2532347","SRR2532348","SRR2532366","SRR2532392","SRR2532324","SRR2532362","SRR2532376","SRR2532384","SRR2532391","SRR2532386","SRR2532375","SRR2532382","SRR2532326","SRR2532342","SRR2532338","SRR2532345","SRR2532370","SRR2532395","SRR2532394","SRR2532341","SRR2532359","SRR2532374","SRR2532351","SRR2532377","SRR2532379","SRR2532385","SRR2532333","SRR2532390","SRR2532334","SRR2532318","SRR2532340","SRR2532378","SRR2532383","SRR2532332","SRR2532343","SRR2532339","SRR2532337","SRR2532350","SRR2532336","SRR2532371","SRR2532335","SRR2532344","SRR2532373","SRR2532381","SRR2532369"]
_SRR_ind=[]
_C=16
first=True
with open(sys.argv[1]) as f:
	for l in f:
		temp=l.split('\n')[0].replace('"','').split(',')
		if first:
			for s in _SRR:
				thisind=temp.index(s)
				if thisind == -1:
					print ERRORR
					break
				else:
					_SRR_ind.append(thisind)
			first=False
		else:
			thisphylo=temp[1]
			if thisphylo == 'NA':
				continue
			thisTid=temp[0]
			totalexp=0
			
			for e in _SRR_ind:
				totalexp=totalexp+float(temp[e])
			avg=totalexp/len(_SRR)
			print thisTid+'\t'+str(avg)+'\t'+thisphylo
		
