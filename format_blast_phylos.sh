#!/bin/bash
#file formats blast output to be used by phylostratr
#read all files
file_dir=$1
file_list=($file_dir/*.out)

#for each file do
for f in "${file_list[@]}"; do
        echo $f
        #keep only selected cols
        #qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore score salltitles qcovs <--- original blast command
        #qseqid sseqid qstart qend sstart send evalue score staxid <--- col heading needed
        #1 2 7 8 9 10 11 13 <-- numbers corresponding to needed cols
        fname=$(basename "$f")
        ext="${fname##*.}"
        fname="${fname%.*}"
        echo $fname
        #split fname into querytxid and staxid
        staxid="$(cut -d'_' -f2 <<<$fname)"
        newfname="$staxid".tab
        echo $staxid
        echo $newfname
        echo "qseqid sseqid qstart qend sstart send evalue score staxid" | tr " " "\t" > $newfname
        awk '{print $1,$2,$7,$8,$9,$10,$11,$13,'"$staxid"'}' $f | head | tr " " "\t" >> $newfname
done
