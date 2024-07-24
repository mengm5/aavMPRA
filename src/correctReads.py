#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# File Name: correctReads.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 21 2024
"""

# conda config --add channels bioconda
# conda config --add channels conda-forge
# conda config --set channel_priority strict
# conda install cutadapt
# cutadapt --version

def rmAdapters(samples, df, inpath, outpath, gzflag):

    ### rmAdapters
    rmAdapters_df = df[df['Steps'] == 'rmAdapters']
    rmAdapters_para = 'cutadapt'
    for i in range(rmAdapters_df.shape[0]):
        rmAdapters_para = rmAdapters_para + ' ' + rmAdapters_df.iloc[i,1] + ' ' + rmAdapters_df.iloc[i,2]
    
    ### command
    cmd = []
    cmd.append('cd '+ outpath)
    for j in range(len(samples)):
        r1 = samples[j] + '_R1.fastq'
        r2 = samples[j] + '_R2.fastq'
        r1_rm1 = samples[j] + '_R1_rm1.fastq'
        r2_rm1 = samples[j] + '_R2_rm1.fastq'
        ut_R1 = samples[j] + '_untrimed_1_rm1.fastq'
        ut_R2 = samples[j] + '_untrimed_2_rm1.fastq'
        logfile = samples[j] + '_rmAdapters.log'
        if gzflag == True:
            tmp_cmd = rmAdapters_para + ' --untrimmed-output ' + ut_R1 + '.gz' + ' --untrimmed-paired-output ' + ut_R2 + '.gz'  + ' -o ' + r1_rm1 + '.gz'  + ' -p ' + r2_rm1 + '.gz'  + ' ' + inpath + '/' + r1 + '.gz'  + ' ' + inpath + '/' + r2 + '.gz'  + ' >' + logfile
        else:
            tmp_cmd = rmAdapters_para + ' --untrimmed-output ' + ut_R1 + ' --untrimmed-paired-output ' + ut_R2 + ' -o ' + r1_rm1 + ' -p ' + r2_rm1 + ' ' + inpath + '/' + r1 + ' ' + inpath + '/' + r2 + ' >' + logfile
        cmd.append(tmp_cmd)
    return(cmd)

def getUMIs(samples, df, inpath, outpath, gzflag):

    ### getUMIs
    getUMIs_df = df[df['Steps'] == 'getUMIs']
    getUMIs_para = 'cutadapt'
    for i in range(getUMIs_df.shape[0]):
        getUMIs_para = getUMIs_para + ' ' + getUMIs_df.iloc[i,1] + ' ' + getUMIs_df.iloc[i,2]
    
    ### command
    cmd = []
    cmd.append('cd ' + outpath)
    for j in range(len(samples)):
        r1_rm1 = samples[j] + '_R1_rm1.fastq'
        r2_rm1 = samples[j] + '_R2_rm1.fastq'
        r1_rm2 = samples[j] + '_R1_rm2.fastq'
        r2_rm2 = samples[j] + '_R2_rm2.fastq'
        ut_R1 = samples[j] + '_untrimed_1_rm2.fastq'
        ut_R2 = samples[j] + '_untrimed_2_rm2.fastq'
        logfile = samples[j] + '_getUMIs.log'
        if gzflag == True:
            tmp_cmd = getUMIs_para + ' --untrimmed-output ' + ut_R1 + '.gz' + ' --untrimmed-paired-output ' + ut_R2 + '.gz' + ' -o ' + r1_rm2 + '.gz' + ' -p ' + r2_rm2 + '.gz' + ' ' + inpath + '/' + r1_rm1 + '.gz' + ' ' + inpath + '/' + r2_rm1 + '.gz' + ' >' + logfile
        else:
            tmp_cmd = getUMIs_para + ' --untrimmed-output ' + ut_R1 + ' --untrimmed-paired-output ' + ut_R2 + ' -o ' + r1_rm2 + ' -p ' + r2_rm2 + ' ' + inpath + '/' + r1_rm1 + ' ' + inpath + '/' + r2_rm1 + ' >' + logfile
        cmd.append(tmp_cmd)
    return(cmd)

def rmUMIs(samples, df, inpath, outpath, gzflag):

    ### getUMIs
    rmUMIs_df = df[df['Steps'] == 'rmUMIs']
    rmUMIs_para = 'cutadapt'
    for i in range(rmUMIs_df.shape[0]):
        rmUMIs_para = rmUMIs_para + ' ' + rmUMIs_df.iloc[i,1] + ' ' + rmUMIs_df.iloc[i,2]
    
    ### command
    cmd = []
    cmd.append('cd ' + outpath)
    for j in range(len(samples)):
        r2_rm1 = samples[j] + '_R2_rm1.fastq'
        r2_umi = samples[j] + '_R2_rmUMI.fastq'
        logfile = samples[j] + '_rmUMIs.log'
        if gzflag == True:
            tmp_cmd = rmUMIs_para + ' -o ' + r2_umi + '.gz' + ' ' + inpath + '/' + r2_rm1 + '.gz' + ' >' + logfile
        else:
            tmp_cmd = rmUMIs_para + ' -o ' + r2_umi + ' ' + inpath + '/' + r2_rm1 + ' >' + logfile
        cmd.append(tmp_cmd)
    return(cmd)


    
    

