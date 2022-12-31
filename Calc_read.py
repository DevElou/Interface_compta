# Fonctions de calcul


# Import
import numpy as np
import pandas as pd

# Ouverture du ficher
file = pd.read_excel("test2.xlsx")

data = pd.DataFrame(file, columns=['Catégorie Dépenses', 'Débit', 'Crédit','SOLDE'])
data = data.fillna(0)

# Fonctions

def credit(open_file):
    cred = 0
    for ele in data.values:
        cred += ele[2]
    return cred


def debit(open_file):
    deb = 0.0
    for ele in data.values:
        if type(ele[1]) == int:
            ele[1] = float(ele[1])
        if ele[1] != np.nan and type(ele[1]) == float or type(ele[1]) == float:
            print(ele[1])
            deb = deb + ele[1]
    return deb


def categorie_dict(open_file):
    dict = {}
    for ele in data.values:
        if not(ele[0] in dict.keys()) and ele[0] != 0:
            dict[ele[0]] = None
    return dict


def depense_dict(dict):
    for cat in dict.keys():
        dep = 0.0
        for ele in data.values:
            if ele[0] == cat :
                if ele[2] > 0.0:
                    dep += float(ele[2])
                if ele[1] > 0.0:
                    dep += -float(ele[1])
        dict[cat] = dep
    return dict



print(depense_dict(categorie_dict(data)))
