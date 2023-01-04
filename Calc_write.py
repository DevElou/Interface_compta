import pandas as pd

import Calc_read as read



def write_solde(open_file,Line):
    open_file.loc[Line, ['SOLDE']] = read.calc_solde(open_file,Line)
def save(open_file,name):
    open_file.to_excel(f"{name}")

#save_path:extension déjà dans le name
def save_path(open_file,name,path):
    out_path = f"{path}\{name}"
    open_file.to_excel(out_path)
def add_line(open_file,date,lib,cat,deb,cred):
    max_ind = open_file.index[-1]
    open_file.loc[max_ind+1] = [date,lib,cat,0,deb,cred,0]

#Set solde de base
def set_solde_init(open_file,solde):
    open_file.loc[0, ['SOLDE']] = float(solde)
    open_file.loc[0, ['Libellé']] = "SOLDE INITIALE"

def recalc_solde(open_file):
    n = len(open_file)
    for i in range(1,n):
        write_solde(open_file,i)







#set_solde_init(read.open,1)
#recalc_solde(read.open)
#print(read.open)








