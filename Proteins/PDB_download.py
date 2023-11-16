

#PBD Download Automation <3

import requests


"""

######### CHANGE TO YOUR FILE PATH BELOW: ##########


"""


FILE_PATH = '/Users/lauramcdonnell/ConiferPoint/'




#Create output file
output_file = open('input.txt', 'w')


#Path to the input file containing groups of PDB IDs
input_file = 'input.tex'

#Read the input file
f = open(input_file, 'r')
lines = f.readlines()

#Read each line -> gets groups of PDB IDs
for line in lines:
    pdb_ids = line.strip().split()
    #initialize a list for each line/group of PDBs
    pdb_filepaths = []

#Loop over each PDB in the group
    for pdb_id in pdb_ids:
        #Get PDB data, save .pdb file
        pdb_url = 'https://files.rcsb.org/download/' + pdb_id + '.pdb'
        data_url = requests.get(pdb_url)
        file = pdb_id + '.pdb'
        open(file, 'wb').write(data_url.content)

        #New file data with filepaths
        pdb_filepath = FILE_PATH + file
        pdb_filepaths.append(pdb_filepath)

    #write output file
    for item in pdb_filepaths:
        output_file.write(item + ' ')

    #creates a new line for each group
    output_file.write('\n')


f.close()
output_file.close()
