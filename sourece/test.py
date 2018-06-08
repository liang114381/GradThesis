import configparser
import os
from rdkit import DataStructs, Chem
from rdkit.Chem import AllChem
import pickle

# class ChEMBL:
#     def __init__(self):
#
#         config = configparser.ConfigParser()
#         config.read('pc.conf')

if __name__ == '__main__':
    mols = Chem.SDMolSupplier(r'D:\Temp\ChEMBL\releases\chembl_01\chembl_01.sdf')

    print(len(mols))

    with open(r'D:\Temp\ChEMBL\releases\chembl_01\chembl_01.pickle', 'wb') as handle:
        pickle.dump(mols[0], handle)
