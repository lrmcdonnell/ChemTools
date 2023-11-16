
%pip install rdkit

import rdkit

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolTransforms


from rdkit.Chem import rdmolfiles
from rdkit.Chem import rdForceFieldHelpers
m = rdmolfiles.MolFromMolFile('/Users/jasonb/before.mol',removeHs=False)
rdForceFieldHelpers.UFFOptimizeMolecule(m)
print(Chem.MolToMolBlock(m))