import os
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import pandas as pd

if __name__ == '__main__':
    infodata_path = os.path.join(r'D:\Temp\data', 'drugbank.tsv')
    sdf_path = os.path.join(r'D:\Temp\data', 'structures.sdf')
    bindingdb_path = os.path.join(r'D:\Temp\data', 'BindingDB_ALL.tsv')
    df = pd.read_csv(infodata_path, sep='\t')
    sdf = Chem.SDMolSupplier(sdf_path)
    bindingdb = pd.read_csv(bindingdb_path, sep='\t', nrows=1000)