import pandas as pd

count_loc = './mycounts_list.txt'
counts = open(count_loc).read() # input file describing the count file names
out_matrix = './counts_matrix.txt'

dict_of_counts = {}
count = counts.split()
for file in count:
    sample = file.split(".cs")[0] # remove extention from file name
    sample = sample.split("_")[1] #remove sample number
    #further name processing may be desired
    dict_of_counts[sample] = {}

    with open(file, "r") as infile:
        next(infile) #skips a line
        #can be done as many times as needed, with the case of read counts likely not needed
        for lines in infile:
            lines = lines.strip().split(",") #adjust for csv or other format if needed
            dict_of_counts[sample][lines[0]] = int(float(lines[1]))

dataframe = pd.DataFrame(dict_of_counts)
dataframe.to_csv(out_matrix, sep='\t')
