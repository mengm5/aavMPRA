#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# File Name: matchByID.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 27 2024
'''
import argparse
import pandas as pd
import csv

def parse_args():
    parser = argparse.ArgumentParser(description = 'Merge several files into one.')

    # Required parameters
    parser.add_argument('samplespath', type = str, help = 'output path(abosolute path).')
    parser.add_argument('samplesname', type = str, help = 'names of several samples (format: sample1,sample2,sample3...), the first column of each file is the ID.')
    parser.add_argument('outpath', type = str, help = 'output path(abosolute path).')
    parser.add_argument('output', type = str, help = 'output file name(tab delimiter).')

    return(parser.parse_args())

def main():
    args = parse_args()
    
    print()
    print('###############################################################################')
    print('Args:')
    print(f'samplespath: {args.samplespath}')
    print(f'samplesname: {args.samplesname}')
    print(f'outpath: {args.outpath}')
    print(f'output: {args.output}')
    print()

    names = args.samplesname.split(',')

    merged_df = pd.DataFrame()
    for name in names:
        print(name)
        tmp_df = pd.read_csv(args.samplespath + '/' + name + '_readCounts.txt', sep = '\t', header = None, names = ['ID', 'Count'])
        # print(tmp_df)
        tmp_df.rename(columns={'Count': name}, inplace = True)
        tmp_df.set_index('ID', inplace = True)
        if merged_df.empty:
            merged_df = tmp_df
        else:
            merged_df = merged_df.join(tmp_df, how = 'outer')
    
    merged_df.fillna(0, inplace = True)
    merged_df.reset_index(inplace = True)
    # print(merged_df)

    merged_df.to_csv(args.outpath + '/' + args.output, sep = '\t', float_format = '%d', index = False, header = True, quoting = csv.QUOTE_NONE, escapechar = ' ')

if __name__ == '__main__':
    main()