#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# File Name: mapReads.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 25 2024
"""

# conda install bowtie
# bowtie-build mm10.fa mm10

def mapReads(samples, df, index, inpath, outpath, gzflag, mode):

    if mode == 'mutagenesis':
        print('mapping reads via bowtie:')
        mapReads_df = df[df['Mode'] == 'mutagenesis']
        mapReads_para = 'bowtie -x ' + index
    if mode == 'common':
        print('mapping reads via bowtie2:')
        mapReads_df = df[df['Mode'] == 'common']
        mapReads_para = 'bowtie2 -x ' + index
    ### mapReads
    mapReads_dff = mapReads_df[mapReads_df['Steps'] == 'mapReads']
    for i in range(mapReads_dff.shape[0]):
        mapReads_para = mapReads_para + ' ' + mapReads_dff.iloc[i,1] + ' ' + mapReads_dff.iloc[i,2]
    
    ### command
    cmd = []
    cmd.append('cd ' + outpath)
    for j in range(len(samples)):
        r1_rm1 = samples[j] + '_R1_rm1.fastq'
        r2_umi = samples[j] + '_R2_rmUMI.fastq'
        sam = samples[j] + '.sam'
        logfile = samples[j] + '_mapReads.log'
        if gzflag == True:
            tmp_cmd = mapReads_para + ' -q -1 ' + inpath + '/' + r1_rm1 + '.gz' + ' -2 ' + inpath + '/' + r2_umi + '.gz' + ' -S ' + sam + ' 2>' + logfile
        else:
            tmp_cmd = mapReads_para + ' -q -1 ' + inpath + '/' + r1_rm1 + ' -2 ' + inpath + '/' + r2_umi + ' -S ' + sam + ' 2>' + logfile
        cmd.append(tmp_cmd)
    return(cmd)
    

