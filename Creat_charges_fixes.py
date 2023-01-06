from tkinter import *
from tkinter import filedialog
import pandas as pd
import Calc_write as fct
import pathlib
import Set_filename
import os
import Calc_read as read
import Data_screen




def open_creators(fenetre):
    directory = filedialog.askdirectory(title="Choisir l'emplacement de votre fichier")
    creators = Toplevel(fenetre)
    creators.geometry("500x500")
    creators.title("Création du fichier de charges fixe")

    def add_line():
        fct.add_line(open_dataframe,date_entry.get(),libelle_entry.get(),cat_entry.get(),Pointe_entry.get(),Debit_entry.get(),Credit_entry.get())
        last_line = len(open_dataframe) - 1
        fct.write_solde(open_dataframe, last_line)

        # Clear tous les champs
        date_entry.delete(0, END)
        libelle_entry.delete(0, END)
        cat_entry.delete(0, END)
        Pointe_entry.delete(0, END)
        Credit_entry.delete(0, END)
        Debit_entry.delete(0, END)


    open_dataframe = pd.DataFrame(columns=['Date', 'Libellé','Catégorie Dépenses', 'Pointé', 'Débit', 'Crédit', 'SOLDE'])
    #fct.add_line(open_dataframe, 0/0/0, "SOLDE INITIALE", "", "", 0, 0)



    add_titre = Label(creators, text="Ajouter un débit ou crédit", font=("Helvetica", 15, "bold"))
    add_titre.place(relx=0.5, rely=0.05, anchor=CENTER)

    # Indication mettre 0 credit ou debit en fonction de l'ajout
    info_add = Label(creators,
                     text=" Ne pas oublié créer le 'SOLDE INITIALE' avec 0 à crédit et 0 à débit ",
                     font=("Helvetica", 7),fg='red')
    info_add.place(relx=0.5, rely=0.1, anchor=CENTER)

    # add Date
    date_lab = Label(creators, text="Date (J/M/A): ")
    date_entry = Entry(creators)
    date_lab.place(relx=0.462, rely=0.16, anchor=CENTER)
    date_entry.place(relx=0.5, rely=0.21, anchor=CENTER)

    # add libelle
    libelle_lab = Label(creators, text="Libellé : ")
    libelle_entry = Entry(creators)
    libelle_lab.place(relx=0.437, rely=0.27, anchor=CENTER)
    libelle_entry.place(relx=0.5, rely=0.32, anchor=CENTER)

    # add catégorie
    cat_lab = Label(creators, text="Catégorie Dépenses : ")
    cat_entry = Entry(creators)
    cat_lab.place(relx=0.492, rely=0.39, anchor=CENTER)
    cat_entry.place(relx=0.5, rely=0.44, anchor=CENTER)

    # add pointé
    Pointe_lab = Label(creators, text="Pointé : ")
    Pointe_entry = Entry(creators)
    Pointe_lab.place(relx=0.439, rely=0.50, anchor=CENTER)
    Pointe_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

    # add debit
    Debit_lab = Label(creators, text="Débit : ")
    Debit_entry = Entry(creators)
    Debit_lab.place(relx=0.434, rely=0.61, anchor=CENTER)
    Debit_entry.place(relx=0.5, rely=0.66, anchor=CENTER)

    # add credit
    Credit_lab = Label(creators, text="Crédit : ")
    Credit_entry = Entry(creators)
    Credit_lab.place(relx=0.434, rely=0.72, anchor=CENTER)
    Credit_entry.place(relx=0.5, rely=0.77, anchor=CENTER)

    # Bouton add_line
    btn_add = Button(creators, text=" Ajouter la ligne ", command=lambda: add_line())
    btn_add.place(relx=0.5, rely=0.87, anchor=CENTER)