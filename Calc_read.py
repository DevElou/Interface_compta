# Fonctions de calcul


# Import
import numpy as np
import pandas as pd

# Ouverture du ficher



def open(name):
    file = pd.read_excel(name)
    data = pd.DataFrame(file, columns=['Date', 'Libellé','Catégorie Dépenses', 'Pointé', 'Débit', 'Crédit', 'SOLDE'])
    data = data.fillna(0)
    return data

# Fonctions

def credit(open_file):
    cred = 0.0
    for ele in open_file.values:
        cred += float(ele[5])
    return cred



def debit(open_file):
    deb = 0.0
    for ele in open_file.values:
        if type(ele[4]) == int:
            ele[4] = float(ele[4])
        if ele[4] != np.nan and type(ele[4]) == float or type(ele[4]) == float:

            deb = deb + ele[4]
    return deb

def categorie_dict(open_file):
    dict = {}
    for ele in open_file.values:
        if not(ele[2] in dict.keys()) and ele[2] != 0:
            dict[ele[2]] = None
    return dict


def depense_dict(dict,open_file):
    for cat in dict.keys():
        dep = 0.0
        for ele in open_file.values:
            if ele[2] == cat :
                if ele[5] > 0.0:
                    dep += float(ele[5])
                if ele[4] > 0.0:
                    dep += -float(ele[4])
        dict[cat] = dep
    return dict

def calc_solde(open_file,Line):
    line = open_file.loc[[Line]]
    line_preced = open_file.loc[[Line-1]]
    solde = 0
    if line.values[0][4] == 0:
        solde = line.values[0][5] + line_preced.values[0][6]
    elif line.values[0][5] == 0:
        solde = line_preced.values[0][6] - line.values[0][4]

    return solde






