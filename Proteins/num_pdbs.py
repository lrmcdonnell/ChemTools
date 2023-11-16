
#Path to the input file containing groups of PDB IDs
input_file = 'input.tex'

#Read the input file
f = open(input_file, 'r')
lines = f.readlines()

num_pdbs = 0

#Read each line -> gets groups of PDB IDs
for line in lines:
    pdb_ids = line.strip().split()
    for pdb_id in pdb_ids:
        num_pdbs += 1

print('Number of PDBs:', num_pdbs)
