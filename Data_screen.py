from tkinter import *
from tkinter.ttk import Treeview

import pandas as pa

#manque scroll bar
def set_filename(fenetre,open_file):
    screen_tab = Toplevel(fenetre)
    screen_tab.geometry("1263x680")
    screen_tab.title("Affichage du tableau")

    # Setting up tkinter window.

    tree = Treeview(screen_tab)

    tree["column"] = list(open_file.columns)
    tree["show"] = "headings"

    for columns in tree["column"]:
        tree.heading(columns,text=columns)
        tree.column(columns,width=180)

    rows = open_file.values.tolist()
    for row in rows:
        tree.insert("","end",values=row)


    tree.grid(row=0, column=0)


