# File_Processing

File_Merger:
Combines various sample files into one matrix
Works with imput files that are 2 column, with the gene description in the first and data in the second. 
Edits the sample file name to name column headers.

First run (assuming input files are in .csv format)

ls *.csv > ./mycounts_list.txt
then run File_Merger.py

To adjust the finished file:
The 10th and 11th line are intended to remove a .csv extention and remove the sample number if it is after an underscore. These can be adjusted to correctly edit the input file names.
The out_matrix variable on the 5th line names the output file, and can be edited to a desired name.
The 16th line skips any lines that are not wanted to be carried over from the input at the beginning of the input files. This can be duplicated or removed to remove the desired number of lines. 


Phenotype_Creator:
Creates a phenotype file for Cibersort with two input files
In the file created uses a 1 to denote the matches and a 2 for every other location. 

Change the both_loc and rpkm_loc to reflect the two files needed and the new_name to reflect the name of the phenotype file you want.
The both_loc file should be a csv file with two columns, the sample name in the first and respective cell type in the second.
The rpkm_loc file should be a csv file in rpkm format of the gene expression data that is intended to be used with cibersort. This is used to get the sample list in the indended order.
