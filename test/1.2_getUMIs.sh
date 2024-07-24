cd /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads
cutadapt -A GCGACGGTCAGAAGACGCTC -U -100 -j 1 --quality-base 28 --untrimmed-output Test1_untrimed_1_rm2.fastq.gz --untrimmed-paired-output Test1_untrimed_2_rm2.fastq.gz -o Test1_R1_rm2.fastq.gz -p Test1_R2_rm2.fastq.gz /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test1_R1_rm1.fastq.gz /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test1_R2_rm1.fastq.gz >Test1_getUMIs.log
cutadapt -A GCGACGGTCAGAAGACGCTC -U -100 -j 1 --quality-base 28 --untrimmed-output Test2_untrimed_1_rm2.fastq.gz --untrimmed-paired-output Test2_untrimed_2_rm2.fastq.gz -o Test2_R1_rm2.fastq.gz -p Test2_R2_rm2.fastq.gz /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test2_R1_rm1.fastq.gz /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test2_R2_rm1.fastq.gz >Test2_getUMIs.log