import csv


type_loc = #add location for type_loc file described in read me
cell_types = open(type_loc).read()
types = cell_types.split()
h = len(types)

sample_loc = #add location for sample_loc file described in read me
samples = open(sample_loc).read()
sample = samples.split()
w = len(sample)

both_loc = #add location for both_loc file described in read me
both = open(both_loc).read() 
pre_dict = both.split()


sample_to_cell = {}

#creates dictionary of samples to the type of cell they consist of
for x in range(len(pre_dict)):
    if x%2==0:
        print('x: ' + pre_dict[x])
        print('x+1: ' + pre_dict[x+1])
        sample_to_cell[pre_dict[x]] = pre_dict[x+1]

#creates matrix of the correct size with '2' in all locations
Matrix = [[2 for x in range(w+1)] for y in range(h+1)]


#adjusts matrix so that a location has a '1' if it matches a sample with the correct cell type
for x in range(len(sample)+1):
    if x != 0:
        Matrix[0][x] = sample[x-1]
    else:
        Matrix[0][x] = "Type"

for x in range(len(types)+1):
    if x != 0:
        Matrix[x][0] = types[x-1]

for h in range(1,len(types)+1):
    for w in range(1,len(sample)+1):
        print('Matrix[0][w]' + Matrix[0][w])
        print('Matrix[h][0]' + Matrix[h][0])
        if sample_to_cell[Matrix[0][w]]==Matrix[h][0]:
            print('yes')
            Matrix[h][w] = 1

#converts matrix to .csv file named Phenotype_Matrix.csv
with open('Phenotype_Matrix.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerows(Matrix)
