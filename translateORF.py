import sys
from Bio.Seq import translate
from Bio import SeqIO
from Bio.Seq import Seq

for record in SeqIO.parse(sys.argv[1], "fasta"):
	print '>'+record.id
	print record.seq.translate()
