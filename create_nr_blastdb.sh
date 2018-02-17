#!/bin/bash

#Submit this script with: sbatch thefilename

#SBATCH -t 5:00:00   # walltime
#SBATCH -N 1   # number of nodes in this job
#SBATCH -n 16   # total number of processor cores in this job

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE

#download nr.gz if not there already
wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nr.gz

#gunzip nr.gz
#faster
pigz -d -p 10 nr.gz
#makeblastdb -in nr -dbtype prot -out nr
#parse_seqids to enable use of GI list
makeblastdb -in nr -title nr -dbtype prot -out nr -parse_seqids
