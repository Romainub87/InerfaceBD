from lib2to3.pgen2.token import LEFTSHIFT
from optparse import Option
import os
from re import match
from tkinter import *
import sqlite3
from tkinter.font import BOLD
from turtle import bgcolor, color, onclick, onkeypress, onscreenclick, pos, position
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ConvertImage import convertImage
from os import listdir
from os.path import isfile, join
from Interface import *
from Menu import *

def openDisplaySolution():
    diplaySolution = Toplevel(window)
    diplaySolution.configure(bg="#ffe599")
    diplaySolution.minsize(width=1400, height=700)
    diplaySolution.maxsize(width=1400, height=700)
    diplaySolution.iconbitmap('Image/logo.ico')
    diplaySolution.title('SensiClimax - CafésPierre/Problematique/Solution')
    menu(diplaySolution)

    lab1 = Label(diplaySolution, text="Solution pour limiter l'empreinte carbone :", bg="#ffe599", font=("Segoe UI Semibold", 12))
    lab1.place(x=30, y=100)
    lab1.config(padx=0)

    lab2 = Label(diplaySolution, text="- Changer de méthode de culture : Utiliser avec parcimoinie les pesticides, arrêter la monoculture", bg="#ffe599", font=("Segoe UI", 12))
    lab2.place(x=30, y=150)
    lab2.config(padx=0)

    lab3 = Label(diplaySolution, text="- Changer de gamme de produit : Proposer une nouvelle gamme plus responsable mais plus coûteux comme le café d'épeautre, sarrasin torréfié ", bg="#ffe599", font=("Segoe UI", 12))
    lab3.place(x=30, y=210)
    lab3.config(padx=0)

    lab4 = Label(diplaySolution, text="- Proposer des filières dit responsable pour accompagner la production du café", bg="#ffe599", font=("Segoe UI", 12))
    lab4.place(x=30, y=260)
    lab4.config(padx=0)

    illustrationLabel = Label(
        diplaySolution,
        image=img, bg="#ffe599"
    )
    illustrationLabel.place(x=1150, y=25)
