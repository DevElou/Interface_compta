import datetime
import Calc_read as read



def write_solde(open_file,Line):
    open_file.loc[Line, ['SOLDE']] = read.calc_solde(open_file,Line)
def save(open_file,name):
    open_file.to_excel(f"{name}")

#save_path:extension déjà dans le name
def save_path(open_file,name,path):
    out_path = f"{path}\{name}"
    open_file.to_excel(out_path)
def add_line(open_file,date,lib,cat,pointe,deb,cred):
    if len(open_file) == 0:
        max_ind = 0
    else:
        max_ind = open_file.index[-1]

    if date == "":
        date_encode = ""
    else:
        date_encode = datetime.datetime.strptime(date,"%d/%m/%Y")
    open_file.loc[max_ind+1] = [date_encode,lib,cat,pointe,deb,cred,0]
    print(open_file)

#Set solde de base
def set_solde_init(open_file,solde):
    open_file.loc[0, ['SOLDE']] = float(solde)
    open_file.loc[0, ['Débit']] = 0
    open_file.loc[0, ['Crédit']] = 0
    open_file.loc[0, ['Libellé']] = "SOLDE INITIALE"

def recalc_solde(open_file):
    n = len(open_file)
    for i in range(1,n):
        write_solde(open_file,i)







#set_solde_init(read.open,1)
#recalc_solde(read.open)
#print(read.open)








