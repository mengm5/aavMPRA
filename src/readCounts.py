#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# File Name: readCounts.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 26 2024
"""

import os
base_path = os.path.dirname(os.path.abspath(__file__))
main_path = base_path.replace('src', 'src/subcode')

# conda install samtools
# conda install bedtools

def extractReadsname(samples, inpath, outpath):

    ### command
    cmd = []
    cmd.append('cd '+ outpath)
    for j in range(len(samples)):
        s1 = samples[j] + '.sam'
        rn1 = samples[j] + '_readsName.txt'
        tmp_cmd = 'perl -alne\' next if $F[0]=~/^@/; print "$F[0]\t$F[2]" if $F[2] ne "*" \' ' + inpath + '/' + s1 + ' | sort -u >' + rn1
        cmd.append(tmp_cmd)
    return(cmd)


def extractUMI(samples, df, inpath, outpath, gzflag):

    umi_len = df[(df['Steps'] == 'rmUMIs') & (df['Name'] == '-u')]
    ### command
    cmd = []
    cmd.append('cd '+ outpath)
    for j in range(len(samples)):
        r = samples[j] + '_R2_rm2.fastq'
        umi = samples[j] + '_UMIs_all.txt'
        new_umi1 = samples[j] + '_UMIs.txt'
        new_umi2 = samples[j] + '_UMIs_rm.txt'
        if gzflag == True:
            tmp_cmd = 'zcat ' + inpath + '/' + r + '.gz' + ' | awk \'NR%4==1 {id=substr($1, 2)} NR%4==2 {print id "\t" $0}\' >' + umi
        else:
            tmp_cmd = 'cat ' + inpath + '/' + r + ' | awk \'NR%4==1 {id=substr($1, 2)} NR%4==2 {print id "\t" $0}\' >' + umi
        cmd.append(tmp_cmd)
        new_tmp_cmd1 = 'cat ' + umi + ' | awk \'{if (length($2) == ' + umi_len.iloc[0,2] + ') print}\' >' + new_umi1
        cmd.append(new_tmp_cmd1)
        new_tmp_cmd2 = 'cat ' + umi + ' | awk \'{if (length($2) != ' + umi_len.iloc[0,2] + ') print}\' >' + new_umi2
        cmd.append(new_tmp_cmd2)
    return(cmd)


def matchPairs(samples, inpath, outpath):

    ### command
    cmd = []
    cmd.append('cd '+ outpath)
    for j in range(len(samples)):
        file1 = samples[j] + '_UMIs.txt'
        file2 = samples[j] + '_readsName.txt'
        outfile = samples[j] + '_matchedPairs.txt'
        tmp_cmd = 'python ' + main_path + '/matchByID.py ' + inpath + '/' + file1 + ' ' + inpath + '/' + file2 + ' ' + outpath + ' ' + outfile
        cmd.append(tmp_cmd)
    return(cmd)

def countUMIs(samples, outpath):

    ### command
    cmd = []
    cmd.append('cd '+ outpath)
    for j in range(len(samples)):
        mf = samples[j] + '_matchedPairs.txt'
        outfile1 = samples[j] + '_uniqueUMIs.txt'
        outfile2 = samples[j] + '_readCounts.txt'
        tmp_cmd1 = 'cat ' + mf + ' | awk \'{print $2, $3}\' OFS=\'\\t\' | sort | uniq >' + outfile1
        cmd.append(tmp_cmd1)
        tmp_cmd2 = 'cat ' + outfile1 + ' | awk \'{print $1}\' | sort | uniq -c | awk \'{print $2 "\t" $1}\' >' + outfile2
        cmd.append(tmp_cmd2)
    return(cmd)

def mergeSamples(samples, inpath, outpath):

    samplesname = ','.join(samples)
    ### command
    cmd = []
    cmd.append('cd '+ outpath)
    tmp_cmd = 'python ' + main_path + '/mergeSamples.py ' + inpath  + ' ' + samplesname + ' ' + outpath + ' mergedSamplesCount.txt'
    cmd.append(tmp_cmd)
    return(cmd)