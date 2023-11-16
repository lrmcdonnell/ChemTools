%pip install rdkit
%pip install psi4

import rdkit
import psi4
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolTransforms

# Create the molecule
smiles = "[n]1c(N)cc[n]c1"
mol = Chem.MolFromSmiles(smiles)
# Generate the initial 3D conformation
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

# Optimize the molecule using B3LYP
# Set the calculation options for B3LYP
psi4.set_options({"basis": "6-311G++", "dft_d": "d3", "geom_opt_max_cycles": 100})
# Convert the RDKit molecule to a Psi4 molecule
psi4_mol = Chem.MolToPDBBlock(mol)
# Optimize the molecule
psi4_mol = psi4.geometry(psi4_mol)
psi4.optimize("b3lyp")
# Update the RDKit molecule with the optimized coordinates
mol = Chem.MolFromPDBBlock(psi4_mol)
rdMolTransforms.CanonicalizeConformer(mol.GetConformer())
# Print the optimized molecule
print(Chem.MolToMolBlock(mol))