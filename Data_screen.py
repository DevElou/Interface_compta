from tkinter import *
from tkinter.ttk import Treeview

import pandas as pa

#manque scroll bar
def tabl_screen(fenetre,open_file):
    screen_tab = Toplevel(fenetre)
    screen_tab.geometry("1192x626")
    screen_tab.title("Affichage du tableau")
    screen_tab.resizable(width=False,height=False)

    # Setting up tkinter window.

    tree = Treeview(screen_tab,height=30)#32
    #scroll = Scrollbar(orient='vertical',command=tree.yview)


    tree["column"] = list(open_file.columns)
    tree["show"] = "headings"

    for columns in tree["column"]:
        tree.heading(columns,text=columns)
        tree.column(columns,width=170)

    rows = open_file.values.tolist()
    for row in rows:
        tree.insert("","end",values=row)


    tree.grid(row=0, column=0)



