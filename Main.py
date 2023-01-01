from tkinter import *
#import Calc_write

# Creation de la fenêtre
fenetre = Tk()
fenetre.title("Interface Comptabilité")
fenetre.geometry("1280x720")
fenetre.resizable(width=False, height=False)

# Frame ajout de ligne
add_Frame = Frame(fenetre)
add_Frame.config(width=640,height=360)
add_Frame.grid(row=0,column=0,sticky="NW")

#Contenu add_Frame
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


cat_lab = Label(add_Frame,text="Catégorie Dépenses : ")
date_entry = Entry(add_Frame)
Pointe_lab = Label(add_Frame,text="Pointé : ")
date_entry = Entry(add_Frame)
Debit_lab = Label(add_Frame,text="Débit : ")
date_entry = Entry(add_Frame)
Credit_lab = Label(add_Frame,text="Crédit : ")
date_entry = Entry(add_Frame)
Solde_lab = Label(add_Frame,text="Solde : ")
date_entry = Entry(add_Frame)


fenetre.mainloop()
