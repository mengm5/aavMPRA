#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# File Name: matchByID.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 27 2024
'''

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = 'Match 2 files via common ID.')

    # Required parameters
    parser.add_argument('file1', type = str, help = 'input file 1 (treat as dictionary) that contains 2 columns(tab delimiter), the first column is ID.')
    parser.add_argument('file2', type = str, help = 'input file 2 that contains 2 columns(tab delimiter), the first column is ID.')
    parser.add_argument('outpath', type = str, help = 'output path(abosolute path).')
    parser.add_argument('output', type = str, help = 'output file name(3 columns with tab delimiter).')

    return(parser.parse_args())

def main():
    args = parse_args()
    
    print()
    print('###############################################################################')
    print('Args:')
    print(f'file1: {args.file1}')
    print(f'file2: {args.file2}')
    print(f'outpath: {args.outpath}')
    print(f'output: {args.output}')
    print()

    file1_dict = {}
    with open(args.file1, 'r') as f:
        for line in f:
            arr = line.strip().split('\t')
            if(len(arr) == 2):
                file1_dict[arr[0]] = arr[1]

    print('########################')
    with open(args.file2, 'r') as f:
        with open(args.outpath + '/' + args.output, 'w', newline = '') as fi:
            for line in f:
                arr = line.strip().split('\t')
                if(len(arr) == 2):
                    if arr[0] in file1_dict:
                        tmp = arr[0] + '\t' + arr[1] + '\t' + file1_dict[arr[0]] + '\n'
                        fi.write(tmp)
    
if __name__ == '__main__':
    main()