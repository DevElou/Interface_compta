from tkinter import *
from tkinter import filedialog
import pathlib
import Calc_write as fct
import pandas as pa


def close(entry,solde_preced):
    path = filedialog.askopenfilename(title="Ouvrir un fichier de charges fixe", defaultextension=".xlsx",
                                      filetypes=[("Xlsx Fichier", ".xlsx")])
    path_parent = pathlib.Path(path).parent.resolve()

    out_path = f"{path_parent}\Suivi_{entry.get()}.xlsx"
    open = fct.read.open(path)
    file = pa.DataFrame(open, columns=['Date', 'Libellé', 'Catégorie Dépenses', 'Pointé', 'Débit', 'Crédit', 'SOLDE'])
    fct.set_solde_init(file,solde_preced)
    fct.recalc_solde(file)
    file.to_excel(out_path)


def set_filename(fenetre):
    creat_suivi = Toplevel(fenetre)
    creat_suivi.geometry("500x150")
    creat_suivi.title("Entrez un nom de fichier")

    label = Label(creat_suivi, text="Mois : ")
    label.place(relx=0.15, rely=0.28)

    entry = Entry(creat_suivi, width=35)
    entry.place(relx=0.36, rely=0.29)

    label_solde = Label(creat_suivi, text="Solde précédent : ")
    label_solde.place(relx=0.15, rely=0.45)

    solde_prec = Entry(creat_suivi, width=35)
    solde_prec.place(relx=0.36, rely=0.45)

    btn_apply = Button(creat_suivi, text=" Ouvriur fichier de charges fixes ",
                       command=lambda: close(entry,float(solde_prec.get())))
    btn_apply.place(relx=0.31, rely=0.73)
