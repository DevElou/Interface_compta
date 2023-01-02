from tkinter import *
from tkinter import filedialog
import pathlib
import Calc_write as fct
import pandas as pa

def close(entry,top):
    path = filedialog.askopenfilename(title="Ouvrir un fichier de charges fixe", defaultextension=".xlsx",
                                      filetypes=[("Xlsx Fichier", ".xlsx")])
    path_parent = pathlib.Path(path).parent.resolve()

    out_path = f"{path_parent}\Suivi_{entry.get()}.xlsx"
    open = fct.read.open(path)
    file = pa.DataFrame(open, columns=['Date', 'Libellé', 'Catégorie Dépenses', 'Pointé', 'Débit', 'Crédit', 'SOLDE'])
    file.to_excel(out_path)


def set_filename(fenetre):
    creat_suivi = Toplevel(fenetre)
    creat_suivi.geometry("500x100")
    creat_suivi.title("Entrez un nom de fichier")

    label = Label(creat_suivi, text="Mois : ")
    label.place(relx=0.03, rely=0.39)

    entry = Entry(creat_suivi, width=35)
    entry.place(relx=0.12, rely=0.4)

    btn_apply = Button(creat_suivi, text=" Ouvriur fichier de charges fixes ", command=lambda: close(entry,creat_suivi))
    btn_apply.place(relx=0.58, rely=0.38)






