cd /data/med-mengm/MPRAproj/MPRA_test3/3_readCounts
perl -alne' next if $F[0]=~/^@/; print "$F[0]	$F[2]" if $F[2] ne "*" ' /data/med-mengm/MPRAproj/MPRA_test3/2_mapReads/Test1.sam | sort -u >Test1_readsName.txt
perl -alne' next if $F[0]=~/^@/; print "$F[0]	$F[2]" if $F[2] ne "*" ' /data/med-mengm/MPRAproj/MPRA_test3/2_mapReads/Test2.sam | sort -u >Test2_readsName.txt