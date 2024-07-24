cd /data/med-mengm/MPRAproj/MPRA_test3/3_readCounts
zcat /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test1_R2_rm2.fastq.gz | awk 'NR%4==1 {id=substr($1, 2)} NR%4==2 {print id "	" $0}' >Test1_UMIs_all.txt
cat Test1_UMIs_all.txt | awk '{if (length($2) == 10) print}' >Test1_UMIs.txt
cat Test1_UMIs_all.txt | awk '{if (length($2) != 10) print}' >Test1_UMIs_rm.txt
zcat /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test2_R2_rm2.fastq.gz | awk 'NR%4==1 {id=substr($1, 2)} NR%4==2 {print id "	" $0}' >Test2_UMIs_all.txt
cat Test2_UMIs_all.txt | awk '{if (length($2) == 10) print}' >Test2_UMIs.txt
cat Test2_UMIs_all.txt | awk '{if (length($2) != 10) print}' >Test2_UMIs_rm.txt