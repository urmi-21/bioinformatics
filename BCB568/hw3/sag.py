# First part of this program will deal with testing whether hypermutation occurs or Not

import sys
import math
from scipy import stats
import re

def readFastaFile(filename):
    fhr=open(filename,"r")
    data=dict()
    seqid=""
    seq=""
    while True:
        line=fhr.readline()
        if not line:
            data[seqid]=seq
            break
        if '>' in line:
            if seqid!="":
                data[seqid]=seq
            seqid=line[1:].strip()
            seq=""
        else:
            seq+=line.strip()
    return data

def computeMLE(data,order,alphabets):
    """
    This function will compute the proportion
    of nucleotides or pair or triades of nucleotides
    as indicated by the provided order. It will return 
    a dictionary where the keys are the nucleotides, or 
    group of nucleotides. This function 
    will also consider overlaps i.e. when the pattern 
    ATAT is searched in the string ATATAT, it will 
    result in two matches.
    """
    probs=dict()
    all_seqs=list(alphabets)
    temp=[]
    prev_seqs=all_seqs.copy()
    for o in range(order-1):
        temp=[]
        for element in prev_seqs:
            for alphabet in alphabets:
                temp.append(element+alphabet)
        prev_seqs=temp.copy()
    all_seqs=prev_seqs
    for seq in all_seqs:
        probs[seq]=0
    total=0
    for seqid in data.keys():
        seq=data[seqid]
        for i in range(len(seq)-order+1):
            substr=seq[i:i+order]
            #print(seq)
            try:
                probs[substr]+=1
            except KeyError:
                print(seqid,substr)
                sys.exit()           
            total+=1
    #count_total=0
    for seq in all_seqs:
        #count_total+=probs[seq]
        probs[seq]=float(probs[seq])/float(total)
    #print(count_total,total)
    return probs
    
def combineTwoFastas(data1,data2):
    """
    This function will take two parameters as input
    which are dictionaries having fasta ids and sequences.
    It will simply combine the two dicitonaries and return the
    combined one.
    """
    return dict(data1,**data2)

def countAlphabetPerSequence(data,alphabets):
    """
    This function will count the occurance of each alphabet
    in each sequence of the provided data set. It will return
    a dictionary where the keys are sequence ids. Each 
    sequence id will point to another dictionary which will have 
    the counts of each element from the alphabet set. This function 
    will also consider overlaps i.e. when the pattern ATAT is searched
    in the string ATATAT, it will result in two matches. All the 
    alphabets searched for must have the same length. 
    """
    lengths=[len(a) for a in alphabets]
    if len(set(lengths))!=1:
        print("All your alphabets must have the same lengths")
        return None
    counts=dict()
    for seqid in data.keys():
        seq=data[seqid]
        counts[seqid]=dict()
        for a in alphabets:
            counts[seqid][a]=0
        for i in range(len(seq)-lengths[0]+1):
            substr=seq[i:i+1]
            counts[seqid][substr]+=1
    return counts

def computeLikelihoodOfWholeData(counts,probs,alphabets):
    """
    This function will compute Likelihood of the 
    whole data set. Unfortunately the likelihood is 
    extremely small and will return a zero.
    """ 
    l=1    
    for seqid in counts.keys():
        #alphabets=counts[seqid]
        for alphabet in alphabets:
            l*=(probs[alphabet]**counts[seqid][alphabet])
            print(probs[alphabet],counts[seqid][alphabet],probs[alphabet]**counts[seqid][alphabet])
    return l

def calculateLogLambda(normal_mles,hyper_mles,combined_mles,nx,hx,alphabets):
    """
    This function will return the value of -2log(lambda)
    """
    loglambda=0
    for alphabet in alphabets:
        print(alphabet,math.log(combined_mles[alphabet]/normal_mles[alphabet]),sum([nx[seqid][alphabet] for seqid in nx.keys()]),math.log(combined_mles[alphabet]/normal_mles[alphabet])*sum([nx[seqid][alphabet] for seqid in nx.keys()]))
        loglambda+=math.log(combined_mles[alphabet]/normal_mles[alphabet])*sum([nx[seqid][alphabet] for seqid in nx.keys()])
    print("="*50)
    for alphabet in alphabets:
        print(alphabet,math.log(combined_mles[alphabet]/hyper_mles[alphabet]),sum([hx[seqid][alphabet] for seqid in hx.keys()]),math.log(combined_mles[alphabet]/hyper_mles[alphabet])*sum([hx[seqid][alphabet] for seqid in hx.keys()]))
        loglambda+=math.log(combined_mles[alphabet]/hyper_mles[alphabet])*sum([hx[seqid][alphabet] for seqid in hx.keys()])
        
    return -2*loglambda

def tsplit(string, delimiters):
    """Behaves str.split but supports multiple delimiters."""
    
    delimiters = tuple(delimiters)
    stack = [string,]
    
    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)
            
    return stack

def splitSequence(seq,seqid):
    """
    This function will split up a single sequence 
    when it encounters spurious alphabets
    """
    splits=dict()
    all_alphabets=set(seq)
    spurious_alphabets=all_alphabets.difference(('A','T','G','C'))
    #print(spurious_alphabets)
    seqsplit=tsplit(seq,spurious_alphabets)
    for i in range(len(seqsplit)):
        splits[seqid+"_"+str(i)]=seqsplit[i]
    #print(splits)
    return splits
    
def purgeData(data):
    """
    This function will take a dictionary of sequences
    as input. It will split the sequences when it encounters
    an alphabet other than 'A','T','G' and 'C'
    """
    updated_dict=dict()
    for seqid in data.keys():
        if len(set(data[seqid]))!=4:
            splits=splitSequence(data[seqid],seqid)
            #data.pop(seqid)
            updated_dict.update(splits)
        else:
            updated_dict[seqid]=data[seqid]
    return updated_dict

def testToCheckHypermutation(normal,hyper):
    """
    This function will basically compute the MLEs and 
    attempt to infer whether hypermutation occurs in
    the data or not.
    """
    alphabet_set=('A','T','G','C','R','W','Y','M','K','N','S','D')
    normal_mles=computeMLE(normal,1,alphabet_set)
    hyper_mles=computeMLE(hyper,1,alphabet_set)
    combined=combineTwoFastas(normal, hyper)
    combined_mles=computeMLE(combined, 1, alphabet_set)
    print(len(normal),len(hyper),len(normal)+len(hyper),len(combined))
    print(normal_mles['A'],normal_mles['T'],normal_mles['G'],normal_mles['C'])
    print(hyper_mles['A'],hyper_mles['T'],hyper_mles['G'],hyper_mles['C'])
    print(combined_mles['A'],combined_mles['T'],combined_mles['G'],combined_mles['C'])
    interested_alphabet_set=('A','T','G','C')
    alphabet_count_in_normal = countAlphabetPerSequence(normal,interested_alphabet_set)
    alphabet_count_in_hyper = countAlphabetPerSequence(hyper,interested_alphabet_set)
    #print(computeLikelihoodOfWholeData(alphabet_count_in_normal,normal_mles,interested_alphabet_set))
    ts=calculateLogLambda(normal_mles,hyper_mles,combined_mles,alphabet_count_in_normal,alphabet_count_in_hyper,('A','G','T','C'))
    p_val=1-stats.chi2.pdf(ts,2)
    print(ts,p_val)

N=readFastaFile("normal.renamed.fa")
N=purgeData(N)
H=readFastaFile("hypermutants.renamed.fa")
H=purgeData(H)
testToCheckHypermutation(N, H)   
