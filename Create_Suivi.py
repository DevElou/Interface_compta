from tkinter import *
from tkinter import filedialog
import Calc_write as fct
import pathlib


def open_creat_suivi(path):
    creat_suivi = Toplevel(fenetre)
    creat_suivi.geometry("640x360")
    creat_suivi.title("Creation d'un fichier de suivi")