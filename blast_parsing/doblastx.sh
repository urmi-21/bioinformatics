species=$(cat species)
max_qcov_hsp="30"
max_targets="10"
evalue="1e-20"
query_file=$1

for s in $species
do 
	echo $s
	#Blast human prot file with each species database
	echo blastx -query "$query_file" -db "database/$s.db/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blastx_res_file" -qcov_hsp_perc $max_qcov_hsp -evalue $evalue -num_threads 15 -max_target_seqs 25
	blastx -query "$query_file" -db "database/$s.db/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blastx_res_file" -qcov_hsp_perc $max_qcov_hsp -evalue $evalue -num_threads 16 -max_target_seqs 25
done
