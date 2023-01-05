from tkinter import *
from tkinter import filedialog
import Calc_write as fct
import pathlib
import Set_filename
import os
import Calc_read as read
import Data_screen


#Ouvre fichier et read.open dans global var
def ouvrir():
    global open_file
    open_file = filedialog.askopenfilename(title="Ouvrir un fichier de suivi",defaultextension=".xlsx",filetypes=[("Xlsx Fichier",".xlsx")])

    global path
    path = pathlib.Path(open_file).parent.resolve()

    global data
    data = read.open(open_file)
    err.config(text=f"{open_file}",fg='black')

def creat_suivi(fenetre):
    Set_filename.set_filename(fenetre)

def screenData(fentere):
    Data_screen.set_filename(fentere,data)
def save():
    try:
        data
    except NameError:
        err.config(text="Veuillez ouvrir un fichier")
    else:
        err.config(text="")
        fct.save_path(data,os.path.basename(open_file),path)

def add_line():
    try:
        data
    except NameError:
        err.config(text="Veuillez ouvrir un fichier")
    else:
        fct.add_line(data, date_entry.get(),str(libelle_entry.get()),str(cat_entry.get()),Pointe_entry.get(),int(Debit_entry.get()),int(Credit_entry.get()))
        last_line = len(data) -1
        fct.write_solde(data,last_line)

        #Clear tous les champs
        date_entry.delete(0,END)
        libelle_entry.delete(0,END)
        cat_entry.delete(0,END)
        Pointe_entry.delete(0,END)
        Credit_entry.delete(0,END)
        Debit_entry.delete(0,END)

def affichage_cat():
    try:
        data
    except NameError:
        err.config(text="Veuillez ouvrir un fichier")
    else:
        dico_cat = read.categorie_dict(data)
        dico_all = read.depense_indict(dico_cat, data)
        text = ""
        for (key, value) in dico_all.items():
            text += f"{key} : {value}\n\n"
        cat.config(text=text,font=("Helvetica",13,"bold"))
        solde.config(text=f"Solde restant : {read.get_solde(data)}",font=("Helvetica",10,"bold"))
        tot_depense.config(text=f"Total des dépenses : {read.debit(data)}",font=("Helvetica",10,"bold"))
        tot_gain.config(text=f"Total des gains : {read.credit(data)}",font=("Helvetica",10,"bold"))


# Creation de la fenêtre
fenetre = Tk()
fenetre.title("Interface Comptabilité")
fenetre.geometry("1280x720")
fenetre.resizable(width=False, height=False)

# Frame ajout de ligne
add_Frame = Frame(fenetre)
add_Frame.config(width=640,height=360,highlightbackground="black",highlightthickness=1)
add_Frame.grid(row=1,column=0,sticky="SW")

#Frame import fichier
import_Frame = Frame(fenetre)
import_Frame.config(width=640,height=360,highlightbackground="black",highlightthickness=1)
import_Frame.grid(row=0,column=0,sticky="NW")

#Frame Affichage infos
infos_Frame = Frame(fenetre)
infos_Frame.config(width=640,height=720,highlightbackground="black",highlightthickness=1)
infos_Frame.place(relx=0.5)





#Contenu add_Frame

add_titre = Label(add_Frame,text="Ajouter un débit ou crédit",font=("Helvetica",15,"bold"))
add_titre.place(relx=0.5, rely=0.05, anchor=CENTER)

#Indication mettre 0 credit ou debit en fonction de l'ajout
info_add = Label(add_Frame,text="Si l'ajout est un Crédit alors mettre 0 dans le champ 'Débit', dans le cas cas contraire, mettre 0 dans le champ 'Crédit'. ",font=("Helvetica",7))
info_add.place(relx=0.5, rely=0.1, anchor=CENTER)


#add Date
date_lab = Label(add_Frame,text="Date (J/M/A): ")
date_entry = Entry(add_Frame)
date_lab.place(relx=0.462,rely=0.16,anchor=CENTER)
date_entry.place(relx=0.5,rely=0.21,anchor=CENTER)

#add libelle
libelle_lab = Label(add_Frame,text="Libellé : ")
libelle_entry = Entry(add_Frame)
libelle_lab.place(relx=0.437,rely=0.27,anchor=CENTER)
libelle_entry.place(relx=0.5,rely=0.32,anchor=CENTER)

#add catégorie
cat_lab = Label(add_Frame,text="Catégorie Dépenses : ")
cat_entry = Entry(add_Frame)
cat_lab.place(relx=0.492,rely=0.39,anchor=CENTER)
cat_entry.place(relx=0.5,rely=0.44,anchor=CENTER)

#add pointé
Pointe_lab = Label(add_Frame,text="Pointé : ")
Pointe_entry = Entry(add_Frame)
Pointe_lab.place(relx=0.439,rely=0.50,anchor=CENTER)
Pointe_entry.place(relx=0.5,rely=0.55,anchor=CENTER)


#add debit
Debit_lab = Label(add_Frame,text="Débit : ")
Debit_entry = Entry(add_Frame)
Debit_lab.place(relx=0.434,rely=0.61,anchor=CENTER)
Debit_entry.place(relx=0.5,rely=0.66,anchor=CENTER)

#add credit
Credit_lab = Label(add_Frame,text="Crédit : ")
Credit_entry = Entry(add_Frame)
Credit_lab.place(relx=0.434,rely=0.72,anchor=CENTER)
Credit_entry.place(relx=0.5,rely=0.77,anchor=CENTER)

#Bouton add_line
btn_add = Button(add_Frame,text="Ajouter la ligne",command= lambda: add_line())
btn_add.place(relx=0.5,rely=0.87,anchor=CENTER)



#Contenu import_frame
import_titre = Label(import_Frame,text="Importer un fichier de compte",font=("Helvetica",15,"bold"))
import_titre.place(relx=0.5, rely=0.05, anchor=CENTER)


#Label error(import_Frame)
err = Label(import_Frame,text="",font=("Helvetica",10),fg='red')
err.place(relx=0.5, rely=0.55, anchor=CENTER)

#Boutton ouvrir fichier(import_Frame)
btn_import = Button(import_Frame,text="Ouvrir un fichier de Suivi",command=ouvrir)
btn_import.place(relx=0.5,rely=0.49,anchor=CENTER)

#Boutton save (import_Frame)
btn_save = Button(import_Frame,text=" Sauvegarder le fichier ",command=save)
btn_save.place(relx=0.45,rely=0.96,anchor=CENTER)

#Boutton creation fichier de suivi
btn_create = Button(import_Frame,text=" Créer un fichier de suivi ",command= lambda :creat_suivi(fenetre))
btn_create.place(relx=0.16,rely=0.96,anchor=CENTER)

#Boutton affichage le tableau
btn_tab = Button(import_Frame,text=" Afficher le tableau ",command= lambda : screenData(fenetre))
btn_tab.place(relx=0.68,rely=0.96,anchor=CENTER)

#


#Infos Frame

#Boutton affichage des infos
btn_infos = Button(infos_Frame,text=" Calculer ",command= affichage_cat)
btn_infos.place(relx=0.5,rely=0.96,anchor=CENTER)

#Affichage des catégories
info_infos = Label(infos_Frame,text=" Ne pas oublier de Sauvegarder le fichier pour enregistrer les modifications ",font=("Helvetica",8))
info_infos.place(relx=0.5, rely=0.02, anchor=CENTER)

#Labael affichant les catégories
cat = Label(infos_Frame,text="",font=("Helvetica",10))
cat.place(relx=0.30,rely=0.06)

#Labelle affichant les gains les debits et le solde restant

tot_gain = Label(infos_Frame,text="",font=("Helvetica",10))
tot_gain.place(relx=0.05,rely=0.90)

tot_depense = Label(infos_Frame,text="",font=("Helvetica",10))
tot_depense.place(relx=0.35,rely=0.90)

solde = Label(infos_Frame,text="",font=("Helvetica",10))
solde.place(relx=0.70,rely=0.90)

fenetre.mainloop()
