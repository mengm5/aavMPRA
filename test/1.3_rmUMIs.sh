cd /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads
cutadapt -u 10 -j 1 -o Test1_R2_rmUMI.fastq.gz /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test1_R2_rm1.fastq.gz >Test1_rmUMIs.log
cutadapt -u 10 -j 1 -o Test2_R2_rmUMI.fastq.gz /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test2_R2_rm1.fastq.gz >Test2_rmUMIs.log