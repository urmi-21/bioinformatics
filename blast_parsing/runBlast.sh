#!/bin/bash

#Submit this script with: sbatch thefilename

#SBATCH -t 96:00:00   # walltime
#SBATCH -N 1   # number of nodes in this job
#SBATCH -n 16   # total number of processor cores in this job
# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
#sh doblastp.sh coding_unann_orf_200.fasta
#blastp -query fasta/chrs/orfs/human_ORFs_200 -db database/human.db/human.db -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out orf_human_blast_res_file -evalue 10e-20 -num_threads 16
#blastp -query fasta/chrs/orfs/human_ORFs_200 -db database/human.db/human.db -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out orf_human_blast_res_file -evalue 1e-20 -num_threads 16 -qcov_hsp_perc 80

#sh doblastp.sh /work/LAS/mash-lab/usingh/urmi/human_data/hominoid/faa/human.faa
sh doblastp.sh /work/LAS/mash-lab/usingh/urmi/human_data/hominoid/ensembl/pep/Homo_sapiens.GRCh38.pep.all.fa
