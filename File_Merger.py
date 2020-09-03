import pandas as pd
import sys, getopt
import argparse


### Example uses
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Combine counts files for individual samples into a compiled counts matrix.',
    epilog='''
    Example usage: python File_merger.py -L count_list.txt 
                    OR
                python File_merger.py -S S1.txt S2.txt S3.txt
    ''')
parser.add_argument('-S','--count_set',nargs='*',type=str, help='Counts files, seperated by space. Tab-delimited (.txt) or comma-seperated (.csv) files are accepted',dest='S')
parser.add_argument('-L','--count_list',type=str, help='Text file of count file names, one file per line. Ignored if --exp_set is also specified',dest='L')
args = parser.parse_args()

if args.S is None and args.L is None:
    print(("No count files provided. Now exiting..."))
    quit()

if args.S is not None:
    counts_set = args.S
if args.L is not None:
    counts_file = args.L
out_matrix = './counts_matrix.txt'

# counts_file='counts_list.txt'
# counts_set=None


if args.S is None:
    print("Using pre-compiled list")
    expression_list = open(counts_file).read().split("\n") # input file describing the count file names
    expression_list = [x for x in expression_list if x.strip() != '']
    if expression_list[0].split(".")[-1] == "txt":
        ct = [pd.read_csv(x,header=0,sep='\t') for x in expression_list]
    if expression_list[0].split(".")[-1] == "csv":
        ct = [pd.read_csv(x,header=0,sep=',') for x in expression_list]
else:
    print("Using identified count files")
    expression_list = [x for x in counts_set if x.strip() != '']
    if expression_list[0].split(".")[-1] == "txt":
        ct = [pd.read_csv(x,header=0,sep='\t') for x in expression_list]
    if expression_list[0].split(".")[-1] == "csv":
        ct = [pd.read_csv(x,header=0,sep=',') for x in expression_list]

dict_of_counts = {}
for key,value in zip(expression_list,ct):
    sample=key.split(".")[0]
    # sample = sample.split("_")[1] #remove sample number
    dict_of_counts[sample] = {}
    for index, row in value.iterrows():
        dict_of_counts[sample][row[0].strip()] = int(float(row[-1]))

dataframe = pd.DataFrame(dict_of_counts)
dataframe.to_csv(out_matrix, sep='\t')


