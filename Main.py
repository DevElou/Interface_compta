from tkinter import *
from tkinter import filedialog
import Calc_write as fct
import pathlib


#Ouvre fichier et read.open dans global var
def ouvrir():
    open_path = filedialog.askopenfilename(title="Ouvrir un fichier de compte",defaultextension=".xlsx",filetypes=[("Xlsx Fichier",".xlsx")])
    global path
    path = pathlib.Path(open_path).parent.resolve()
    global data
    data = fct.read.open(open_path)


def save():
    try:
        data
    except NameError:
        err.config(text="Veuillez ouvrir un fichier")
    else:
        err.config(text="")
        fct.save_path(data,"Sauv1",path)


def add_line(data):
    fct.add_line(data, date_entry.get(),str(libelle_entry.get()),str(cat_entry.get()),int(Debit_entry.get()),int(Credit_entry.get()))
    last_line = len(data) -1
    fct.write_solde(data,last_line)


# Creation de la fenêtre
fenetre = Tk()
fenetre.title("Interface Comptabilité")
fenetre.geometry("1280x720")
fenetre.resizable(width=False, height=False)

# Frame ajout de ligne
add_Frame = Frame(fenetre)
add_Frame.config(width=640,height=360,highlightbackground="black",highlightthickness=1)
add_Frame.grid(row=0,column=0,sticky="NW")

#Frame import fichier
import_Frame = Frame(fenetre)
import_Frame.config(width=640,height=360,highlightbackground="black",highlightthickness=1)
import_Frame.grid(row=1,column=0,sticky="SW")


#Contenu add_Frame
#Ajouter aide pr indique mettre 0 credit ou debit
add_titre = Label(add_Frame,text="Ajouter un débit ou crédit",font=("Helvetica",15,"bold"))
add_titre.place(relx=0.5, rely=0.05, anchor=CENTER)


#add Date
date_lab = Label(add_Frame,text="Date : ")
date_entry = Entry(add_Frame)
date_lab.place(relx=0.43,rely=0.15,anchor=CENTER)
date_entry.place(relx=0.5,rely=0.2,anchor=CENTER)

#add libelle
libelle_lab = Label(add_Frame,text="Libellé : ")
libelle_entry = Entry(add_Frame)
libelle_lab.place(relx=0.436,rely=0.26,anchor=CENTER)
libelle_entry.place(relx=0.5,rely=0.31,anchor=CENTER)

#add catégorie
cat_lab = Label(add_Frame,text="Catégorie Dépenses : ")
cat_entry = Entry(add_Frame)
cat_lab.place(relx=0.49,rely=0.38,anchor=CENTER)
cat_entry.place(relx=0.5,rely=0.43,anchor=CENTER)

#add pointé
Pointe_lab = Label(add_Frame,text="Pointé : ")
Pointe_entry = Entry(add_Frame)
Pointe_lab.place(relx=0.439,rely=0.49,anchor=CENTER)
Pointe_entry.place(relx=0.5,rely=0.54,anchor=CENTER)


#add debit
Debit_lab = Label(add_Frame,text="Débit : ")
Debit_entry = Entry(add_Frame)
Debit_lab.place(relx=0.434,rely=0.60,anchor=CENTER)
Debit_entry.place(relx=0.5,rely=0.65,anchor=CENTER)

#add credit
Credit_lab = Label(add_Frame,text="Crédit : ")
Credit_entry = Entry(add_Frame)
Credit_lab.place(relx=0.434,rely=0.71,anchor=CENTER)
Credit_entry.place(relx=0.5,rely=0.76,anchor=CENTER)

#Bouton add_line
btn_add = Button(add_Frame,text="Ajouter la ligne",command= lambda: add_line(data))
btn_add.place(relx=0.5,rely=0.86,anchor=CENTER)

#Contenu import_frame
#Ajouter label importance etape 1
import_titre = Label(import_Frame,text="Importer un fichier de compte",font=("Helvetica",15,"bold"))
import_titre.place(relx=0.5, rely=0.05, anchor=CENTER)

#Label error(import_Frame)
err = Label(import_Frame,text="",font=("Helvetica",10),fg='red')
err.place(relx=0.5, rely=0.55, anchor=CENTER)

#Boutton ouvrir fichier(import_Frame)
btn_import = Button(import_Frame,text="Ouvrir un fichier de compte",command=ouvrir)
btn_import.place(relx=0.5,rely=0.49,anchor=CENTER)

#Boutton save (import_Frame)
btn_save = Button(import_Frame,text=" Sauvegarder le fichier ",command=save)
btn_save.place(relx=0.5,rely=0.96,anchor=CENTER)


fenetre.mainloop()
