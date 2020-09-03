import csv

'''
INPUTS:
'''
new_name = #File name for new phenotype file, with .csv extention
both_loc = #Location of csv file with two columns,the sample name
           #in the first and respective cell type in the second
rpkm_loc = #Location of gene expression data in rpkm format, the file
           #to be input into


both = open(both_loc).read()
print (both)
pre_dict = both.split()


sample_to_cell = {}

#creates dictionary of samples to the type of cell they consist of
for x in range(len(pre_dict)):
    if x%2==0:
        #print('x: ' + pre_dict[x])
        #print('x+1: ' + pre_dict[x+1])
        #print('first')
        #print(x/2)
        sample_to_cell[pre_dict[x]] = pre_dict[x+1]

cell_to_sample = {}

#creates dictionary of samples to the type of cell they consist of
for x in range(len(pre_dict)):
    if x%2==0:
        #print('x: ' + pre_dict[x])
        #print('x+1: ' + pre_dict[x+1])
        #print('second')
        #print(x/2)
        cell_to_sample[pre_dict[x+1]] = pre_dict[x]

#print(cell_to_sample.keys())
print(list(cell_to_sample.keys()))
types = list(cell_to_sample.keys())
h = len(types)
#print (types)

rpkm = open(rpkm_loc).read()
pre_dict = rpkm.split('\n')
sample = pre_dict[0]
samples = sample.split()[1:]c
w = len(samples)


#creates matrix of the correct size with '2' in all locations
Matrix = [[2 for x in range(w+1)] for y in range(h+1)]


#adjusts matrix so that a location has a '1' if it matches a sample with the correct cell type
for x in range(len(samples)+1):
    if x != 0:
        Matrix[0][x] = samples[x-1]
    else:
        Matrix[0][x] = "Type"

for x in range(len(types)+1):
    if x != 0:
        Matrix[x][0] = types[x-1]

for h in range(1,len(types)+1):
    for w in range(1,len(samples)+1):
        print('Matrix[0][w]' + Matrix[0][w])
        print('Matrix[h][0]' + Matrix[h][0])
        if sample_to_cell[Matrix[0][w]]==Matrix[h][0]:
            print('yes')
            Matrix[h][w] = 1

#converts matrix to .csv file named Phenotype_Matrix.csv
with open(new_name, 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerows(Matrix)
