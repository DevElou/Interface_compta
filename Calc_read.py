# Fonctions de calcul


# Import
import numpy as np
import pandas as pd

# Ouverture du ficher

fichier = "Suivi.xlsx"

def open(name):
    file = pd.read_excel(name)
    data = pd.DataFrame(file, columns=['Catégorie Dépenses', 'Débit', 'Crédit', 'SOLDE'])
    data = data.fillna(0)
    return data

data = open(fichier)

# Fonctions

def credit(open_file):
    cred = 0
    for ele in open_file.values:
        cred += ele[2]
    return cred


def debit(open_file):
    deb = 0.0
    for ele in open_file.values:
        if type(ele[1]) == int:
            ele[1] = float(ele[1])
        if ele[1] != np.nan and type(ele[1]) == float or type(ele[1]) == float:
            print(ele[1])
            deb = deb + ele[1]
    return deb

def categorie_dict(open_file):
    dict = {}
    for ele in open_file.values:
        if not(ele[0] in dict.keys()) and ele[0] != 0:
            dict[ele[0]] = None
    return dict


def depense_dict(dict,open_file):
    for cat in dict.keys():
        dep = 0.0
        for ele in open_file.values:
            if ele[0] == cat :
                if ele[2] > 0.0:
                    dep += float(ele[2])
                if ele[1] > 0.0:
                    dep += -float(ele[1])
        dict[cat] = dep
    return dict

def calc_solde(open_file,Line):
    line = open_file.loc[[Line]]
    line_preced = open_file.loc[[Line-1]]
    solde = 0
    if line.values[0][1] == 0:
        solde = line.values[0][2] + line_preced.values[0][3]
    elif line.values[0][2] == 0:
        solde = line_preced.values[0][3] - line.values[0][1]

    return solde






