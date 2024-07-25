cd /data/med-mengm/MPRAproj/MPRA_test3/3_readCounts
cat Test1_matchedPairs.txt | awk '{print $2, $3}' OFS='\t' | sort | uniq >Test1_uniqueUMIs.txt
cat Test1_uniqueUMIs.txt | awk '{print $1}' | sort | uniq -c | awk '{print $2 "	" $1}' >Test1_readCounts.txt
cat Test2_matchedPairs.txt | awk '{print $2, $3}' OFS='\t' | sort | uniq >Test2_uniqueUMIs.txt
cat Test2_uniqueUMIs.txt | awk '{print $1}' | sort | uniq -c | awk '{print $2 "	" $1}' >Test2_readCounts.txt