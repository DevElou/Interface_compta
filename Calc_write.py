import Calc_read as read
import os


def write_solde(open_file,Line):
    open_file.loc[Line, ['SOLDE']] = read.calc_solde(open_file,Line)

def save(open_file,name):
    open_file.to_excel(f"{name}.xlsx")
def save_path(open_file,name,path):
    out_path = f"{path}\{name}.xlsx"
    open_file.to_excel(out_path)
def add_line(open_file,date,lib,cat,deb,cred):
    max_ind = open_file.index[-1]
    open_file.loc[max_ind+1] = [date,lib,cat,0,deb,cred,0]









