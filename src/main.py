#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# File Name: main.py
# Author: MengM
# mail: mengm5@mail2.sysu.edu.cn 
# Created Time: June 21 2024
'''

import os
import sys
import argparse
import pandas as pd
from datetime import datetime

def get_base_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.join(os.path.dirname(sys.executable), 'src')
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return base_path

base_path = get_base_path()
# print("Base path:", base_path)
sys.path.append(base_path)

import softlinks
import correctReads
import mapReads
import readCounts

def parse_args():
    parser = argparse.ArgumentParser(description = 'aavMPRA program')

    # Required
    parser.add_argument('-o', '--out_path', type = str, help = 'output path (absolute path is recommended) to run workflow, must be provided.')
    parser.add_argument('-f', '--fastq_info', type = str, help = 'fastq_info.txt that contains fastq information must be provided, e.g. /aavMPRA/data/fastq_info.txt.')
    parser.add_argument('-p', '--parameter', type = str, help = 'parameter.txt that contains parameters must be provided, e.g. /aavMPRA/data/parameter.txt.')
    parser.add_argument('-m', '--mode', type = str, help = 'mapping mode: mutagenesis or common. The mutagenesis mode uses bowtie, and the common mode uses bowtie2.')
    parser.add_argument('-i', '--bowtie_index', type = str, help = '/path_to_bowtie_index/bowtie_index_name (absolute path is recommended). e.g. /aavMPRA/index/mutagenesis_index/mutagenesis.')
    parser.add_argument('--gz', action = 'store_true', default = 'False', help = 'if the fastq file saved as .gz file, please add this parameter.')

    return(parser.parse_args())

def main():
    args = parse_args()

    print()
    print('###############################################################################')
    print('Args:')
    if args.out_path:
        print(f'Output path provided: {args.out_path}')
    else:
        print('No output path specified.')
    if args.fastq_info:
        print(f'Fastq information provided: {args.fastq_info}')
    else:
        print('Fastq information specified.')
    if args.parameter:
        print(f'Parameter provided: {args.parameter}')
    else:
        print('Parameter specified.')
    if args.mode:
        print(f'Mode provided: {args.mode}')
    else:
        print('No Mode specified.')
    if args.bowtie_index:
        print(f'Bowtie index provided: {args.bowtie_index}')
    else:
        print('Bowtie index specified.')

    print(f'if gz: {args.gz}')
    print()

    ###############################################################################
    #  global
    ###############################################################################

    save_time = []
    tmptime = 'steps\tstart_time\tend_time\tinterval'
    save_time.append(tmptime)
    fastq_info_df = pd.read_csv(args.fastq_info, sep = '\t')
    # print(fastq_info_df)
    parameter_df = pd.read_csv(args.parameter, sep = '\t')
    # print(parameter_df)
    samples = fastq_info_df.iloc[:, 2].unique()
    # print(samples)

    ###############################################################################
    #  0 makeSoftlinks
    ###############################################################################

    print('###############################################################################')
    print('Generating softlinks for FASTQs.\n')
    start_time = datetime.now()
    start_time_f = start_time.strftime("%Y-%m-%d %H:%M:%S")
    print('Start at: ' + start_time_f + '\n')

    ############################## mkdir
    softlink_path = args.out_path + '/0_softlinks'
    if not os.path.exists(softlink_path):
        print('mkdir ' + softlink_path)
        os.system('mkdir ' + softlink_path)
    else:
        print(softlink_path + ' exists!')
    
    ############################## softlinks
    if not os.path.exists(args.out_path + '/0_softlink.sh'):
        command = softlinks.makeSoftlinks(fastq_info_df, softlink_path, args.gz)
        out_command = '\n'.join(command)
        with open(args.out_path + '/0_softlink.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/0_softlink.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/0_softlink.sh')
    os.system('bash ' + args.out_path + '/0_softlink.sh')
    print()

    end_time = datetime.now()
    end_time_f = end_time.strftime("%Y-%m-%d %H:%M:%S")
    print('End at: ' + end_time_f + '\n')

    time_diff = end_time - start_time
    print('Time interval:')
    print(time_diff)

    tmptime =  '0_softlink\t' + str(start_time) + '\t' + str(end_time) + '\t' + str(time_diff)
    save_time.append(tmptime)

    ###############################################################################
    #  1 correctReads
    ###############################################################################

    print('###############################################################################')
    print('Correct read structure.\n')
    start_time = datetime.now()
    start_time_f = start_time.strftime("%Y-%m-%d %H:%M:%S")
    print('Start at: ' + start_time_f + '\n')

    ############################## mkdir
    correctReads_path = args.out_path + '/1_correctReads'
    if not os.path.exists(correctReads_path):
        print('mkdir ' + correctReads_path)
        os.system('mkdir ' + correctReads_path)
    else:
        print(correctReads_path + ' exists!')
    
    ############################## rmAdapters
    if not os.path.exists(args.out_path + '/1.1_rmAdapters.sh'):
        command = correctReads.rmAdapters(samples, parameter_df, softlink_path, correctReads_path, args.gz)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/1.1_rmAdapters.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/1.1_rmAdapters.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/1.1_rmAdapters.sh')
    os.system('bash ' + args.out_path + '/1.1_rmAdapters.sh')
    print()

    ############################## getUMIs
    if not os.path.exists(args.out_path + '/1.2_getUMIs.sh'):
        command = correctReads.getUMIs(samples, parameter_df, correctReads_path, correctReads_path, args.gz)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/1.2_getUMIs.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/1.2_getUMIs.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/1.2_getUMIs.sh')
    os.system('bash ' + args.out_path + '/1.2_getUMIs.sh')
    print()

    ############################## rmUMIs
    if not os.path.exists(args.out_path + '/1.3_rmUMIs.sh'):
        command = correctReads.rmUMIs(samples, parameter_df, correctReads_path, correctReads_path, args.gz)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/1.3_rmUMIs.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/1.3_rmUMIs.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/1.3_rmUMIs.sh')
    os.system('bash ' + args.out_path + '/1.3_rmUMIs.sh')
    print()

    end_time = datetime.now()
    end_time_f = end_time.strftime("%Y-%m-%d %H:%M:%S")
    print('End at: ' + end_time_f + '\n')

    time_diff = end_time - start_time
    print('Time interval:')
    print(time_diff)

    tmptime = '1_correctReads\t' + str(start_time) + '\t' + str(end_time) + '\t' + str(time_diff)
    save_time.append(tmptime)

    ###############################################################################
    #  2 mapReads
    ###############################################################################

    print('###############################################################################')
    print('Map reads to index.\n')
    start_time = datetime.now()
    start_time_f = start_time.strftime("%Y-%m-%d %H:%M:%S")
    print('Start at: ' + start_time_f + '\n')

    ############################## mkdir
    mapReads_path = args.out_path + '/2_mapReads'
    if not os.path.exists(mapReads_path):
        print('mkdir ' + mapReads_path)
        os.system('mkdir ' + mapReads_path)
    else:
        print(mapReads_path + ' exists!')
    
    ############################## mapReads
    if not os.path.exists(args.out_path + '/2_mapReads.sh'):
        command = mapReads.mapReads(samples, parameter_df, args.bowtie_index, correctReads_path, mapReads_path, args.gz, args.mode)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/2_mapReads.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/2_mapReads.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/2_mapReads.sh')
    os.system('bash ' + args.out_path + '/2_mapReads.sh')
    print()

    end_time = datetime.now()
    end_time_f = end_time.strftime("%Y-%m-%d %H:%M:%S")
    print('End at: ' + end_time_f + '\n')

    time_diff = end_time - start_time
    print('Time interval:')
    print(time_diff)

    tmptime = '2_mapReads\t' + str(start_time) + '\t' + str(end_time) + '\t' + str(time_diff)
    save_time.append(tmptime)

    
    ###############################################################################
    #  3 readCounts
    ###############################################################################

    print('###############################################################################')
    print('Generate readcounts.\n')
    start_time = datetime.now()
    start_time_f = start_time.strftime("%Y-%m-%d %H:%M:%S")
    print('Start at: ' + start_time_f + '\n')

    ############################## mkdir
    readCounts_path = args.out_path + '/3_readCounts'
    if not os.path.exists(readCounts_path):
        print('mkdir ' + readCounts_path)
        os.system('mkdir ' + readCounts_path)
    else:
        print(readCounts_path + ' exists!')

    ############################## extractReadsname
    if not os.path.exists(args.out_path + '/3.1_extractReadsname.sh'):
        command = readCounts.extractReadsname(samples, mapReads_path, readCounts_path)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/3.1_extractReadsname.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/3.1_extractReadsname.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/3.1_extractReadsname.sh')
    os.system('bash ' + args.out_path + '/3.1_extractReadsname.sh')
    print()

    ############################## extractUMI
    if not os.path.exists(args.out_path + '/3.2_extractUMI.sh'):
        command = readCounts.extractUMI(samples, parameter_df, correctReads_path, readCounts_path, args.gz)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/3.2_extractUMI.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/3.2_extractUMI.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/3.2_extractUMI.sh')
    os.system('bash ' + args.out_path + '/3.2_extractUMI.sh')
    print()

    ############################## matchPairs
    if not os.path.exists(args.out_path + '/3.3_matchPairs.sh'):
        command = readCounts.matchPairs(samples, readCounts_path, readCounts_path)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/3.3_matchPairs.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/3.3_matchPairs.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/3.3_matchPairs.sh')
    os.system('bash ' + args.out_path + '/3.3_matchPairs.sh')
    print()

    ############################## countUMIs
    if not os.path.exists(args.out_path + '/3.4_countUMIs.sh'):
        command = readCounts.countUMIs(samples, readCounts_path)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/3.4_countUMIs.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/3.4_countUMIs.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/3.4_countUMIs.sh')
    os.system('bash ' + args.out_path + '/3.4_countUMIs.sh')
    print()

    ############################## mergeSamples
    if not os.path.exists(args.out_path + '/3.5_mergeSamples.sh'):
        command = readCounts.mergeSamples(samples, readCounts_path, readCounts_path)
        print(command)
        out_command = '\n'.join(command)
        with open(args.out_path + '/3.5_mergeSamples.sh', 'w', newline = '') as fi:
            fi.write(out_command)
    else:
        print(args.out_path + '/3.5_mergeSamples.sh exists!')
    print()
    
    print('Run:')
    print('bash ' + args.out_path + '/3.5_mergeSamples.sh')
    os.system('bash ' + args.out_path + '/3.5_mergeSamples.sh')
    print()

    end_time = datetime.now()
    end_time_f = end_time.strftime("%Y-%m-%d %H:%M:%S")
    print('End at: ' + end_time_f + '\n')

    time_diff = end_time - start_time
    print('Time interval:')
    print(time_diff)

    tmptime = '3_readCounts\t' + str(start_time) + '\t' + str(end_time) + '\t' + str(time_diff)
    save_time.append(tmptime)

    out_command = '\n'.join(save_time)
    with open(args.out_path + '/time.txt', 'w', newline = '') as fi:
        fi.write(out_command)



if __name__ == '__main__':
    main()
