species=$(cat species)
max_qcov_hsp="30"
max_targets="10"
evalue="1e-4"
query_file=$1

#for s in $species
#do 
#	echo $s
	#Blast human prot file with each species database
#	echo blastp -query "$query_file" -db "database/$s.db/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blast_res_file_default" -qcov_hsp_perc $max_qcov_hsp -evalue $evalue -num_threads 15 -max_target_seqs 25
#	blastp -query "$query_file" -db "database/$s.db/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blast_res_file_ensmbl" -qcov_hsp_perc $max_qcov_hsp -evalue $evalue -num_threads 16 -max_target_seqs 25
	#blastp -query "$query_file" -db "database/$s.db/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blastp_res_file_default" -evalue $evalue -num_threads 16 -max_target_seqs 25
#done

#do blastp with ensembl database
species=$(cat species_ensembl)
for s in $species
do
        echo $s
        #Blast human prot file with each species database
        echo blastp -query "$query_file" -db "database/$s/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blast_res" -qcov_hsp_perc $max_qcov_hsp -evalue $evalue -num_threads 15 -max_target_seqs 25
       blastp -query "$query_file" -db "database/$s/$s.db" -outfmt '6 qseqid sseqid pident evalue qcovs qcovhsp score bitscore qframe sframe' -out "$s""_blast_res_10-4" -evalue $evalue -num_threads 16 -max_target_seqs 25
done
