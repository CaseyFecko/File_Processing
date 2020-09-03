import csv
import pandas as pd
import sys, getopt
import argparse

### Example uses
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Combine counts files for individual samples into a compiled counts matrix.',
    epilog='''
    Example usage: python Phenotype_creator.py -R RPKM.txt -CT cell_type.txt --output_prefix ./Pheno_matrix
                    OR
                python Phenotype_creator.py -R RPKM.csv -CT cell_type.csv
    ''')
optional = parser._action_groups.pop() # Edited this line
requiredNamed = parser.add_argument_group('Required arguments')
requiredNamed.add_argument('-R','--rpkm',type=str, help='RPKM file (describe structure more here). Tab-delimited (.txt) or comma-seperated (.csv) text files are accepted',dest='r',required=True)
requiredNamed.add_argument('-CT','--cell_type',type=str, help='csv file with two columns,the sample name in the first and respective cell type in the second',dest='ct',required=True)
optional.add_argument('-OUT','--output_prefix',type=str, help='File name prefix for resulting phenotype file. ".txt" is automatically added',dest='out')
parser._action_groups.append(optional) # added this line
args = parser.parse_args()

# Define variables from argument list
rpkm = args.r
ct = args.ct
if args.out is not None:
    outfile = args.out
else:
    outfile = "./Phenotype_matrix"

# rpkm="./test/GSE125197_rpkm_minimal.txt"
# ct="./test/metadata_example.csv"
# python Phenotype_Creator.py -R ./test/GSE125197_rpkm_minimal.txt -CT ./test/metadata_example.csv --output_prefix ./P_mat

if ct.split(".")[-1] == "txt":
    both = pd.read_csv(ct,header=0,sep='\t')
elif ct.split(".")[-1] == "csv":
    both = pd.read_csv(ct,header=0,sep=',')

if rpkm.split(".")[-1] == "txt":
    rpkm = pd.read_csv(rpkm,header=0,sep='\t')
elif rpkm.split(".")[-1] == "csv":
    rpkm = pd.read_csv(rpkm,header=0,sep=',')

#Format RPKM columns
new_columns = [x.strip() for x in rpkm.columns.values]; new_columns[0] = "gene_id"; rpkm.columns  = new_columns
# Extract RPKM columns
cs = rpkm.columns.values[1:]
both_cols = both.columns.values
# Identify unique cell types 
cell_types = both[both_cols[1]].unique()
# Generate matrix
w=len(cs)
h=len(cell_types)

df = pd.DataFrame([[2 for x in range(w)] for y in range(h)])
df.columns = cs
df.set_index(cell_types,inplace=True) 

both_sub=both[both[both_cols[0]].isin(cs)]

for i, val in both_sub.iterrows():
    # print(i)
    # print(val[1]+"; "+val[0])
    df.loc[val[1],val[0]] = 1

file_name = outfile+".txt"
df.to_csv(file_name,sep="\t",index=True)

