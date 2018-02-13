#!/usr/bin/env python
#split single fasta into many

from __future__ import division
import sys
import math
import re
from Bio import SeqIO
from Bio.Seq import Seq
import regex as re
import time
from random import randint

for record in SeqIO.parse(sys.argv[1], "fasta"):
	seqid=record.id
	print seqid,
	print len(record.seq)
	
	SeqIO.write(record, seqid, "fasta")
