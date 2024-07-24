cd /data/med-mengm/MPRAproj/MPRA_test3/2_mapReads
bowtie -x /data/med-mengm/MPRAproj/aavMPRA/index/mutagenesis_index/mutagenesis -m 1 -n 2 -p 1 --chunkmbs 512 -q -1 /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test1_R1_rm1.fastq.gz -2 /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test1_R2_rmUMI.fastq.gz -S Test1.sam 2>Test1_mapReads.log
bowtie -x /data/med-mengm/MPRAproj/aavMPRA/index/mutagenesis_index/mutagenesis -m 1 -n 2 -p 1 --chunkmbs 512 -q -1 /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test2_R1_rm1.fastq.gz -2 /data/med-mengm/MPRAproj/MPRA_test3/1_correctReads/Test2_R2_rmUMI.fastq.gz -S Test2.sam 2>Test2_mapReads.log