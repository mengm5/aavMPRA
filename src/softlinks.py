#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# File Name: softlinks.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 21 2024
"""

def makeSoftlinks(df, path, gzflag):
    cmd = []
    for i in range(df.shape[0]):
        fq_path = df.iloc[i,0]
        fq_name = df.iloc[i,1]
        fq_rename = df.iloc[i,2]
        fq_read = df.iloc[i,3]
        if gzflag == True:
            tmp_cmd = 'ln -s ' + fq_path + '/' + fq_name + ' ' + path + '/' + fq_rename + '_' + fq_read + '.fastq.gz'
        else:
            tmp_cmd = 'ln -s ' + fq_path + '/' + fq_name + ' ' + path + '/' + fq_rename + '_' + fq_read + '.fastq'
        cmd.append(tmp_cmd)
    return(cmd)
        
        
# softlink(file_path, main_path, out_path)

    
    

