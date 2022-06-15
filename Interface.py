from lib2to3.pgen2.token import LEFTSHIFT
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


# Contenu menu déroulant
OptionList = [
    "Map of the World",
    "Area repartition in Nouvelle-Aquitaine",
    "Afficher historique 30 ans du PIB pour chaque Pays",
    "Comparaison des bilans avec conséquence climatique",
    "Causes et origines des émissions des GES",
    "Afficher nombres d'habitant par pays",
    "Empreinte carbone du pays"
]

# Permet de savoir quelle action veut l'utilisateur


def choix_action():
    match OptionList.index(variable.get())+1:
        case 1:
            Action1()
        case 2:
            Action2()
        case 3:
            Action3()
        case 4:
            Action4()
        case 5:
            Action5()
        case 6:
            Action6()
        case 7:
            Action7()

# Permet de d'afficher le graphe converti


def Action1():
    labelAction.config(image=pie)

# Permet d'afficher un planisfère


def Action2():
    labelAction.config(image=map)


def Action3():
    pass


def Action4():
    pass


def Action5():
    pass


def Action6():
    pass


def Action7():
    pass


# Init1isation de l'interface Tkinter
window = Tk()
window.minsize(width=1400, height=700)
window.maxsize(width=1400, height=700)
window.configure(bg="#ffe599")
window.iconbitmap('Image/logo.ico')
window.geometry("1920x1080")
window.title('SensiClimax - CafésPierre')

'''Récupération des images des graphiques qui seront utilisés'''
# planisfère
map = PhotoImage(file=convertImage("Image/figure.png"))

# graphique type camembert
pie = PhotoImage(file="Image/modele.png")

exemple = Image.open(convertImage("Image/Pie.png"))
exemple = exemple.resize((200, 175), Image.ANTIALIAS)
imgExemple = ImageTk.PhotoImage(exemple)

mamie = Image.open("./Image/Mamie.png")
mamie = mamie.resize((430, 270), Image.ANTIALIAS)
imgMamie = ImageTk.PhotoImage(mamie)

chart = Image.open(convertImage("./Image/chart.png"))
chart = chart.resize((300, 300), Image.ANTIALIAS)
imgChart = ImageTk.PhotoImage(chart)

# Titre de la fenêtre
my_label = Label(text="Bienvenue", bg="#ffe599", fg="Black",
                 font=("FARRAY", 40))  # setting up the labels
my_label.pack()

# Création du contenu de la fenêtre
labelAction = Label(window, image=None, bg="#ffe599")
labelAction.place(x=290, y=150, width=800, height=500)

image = Image.open("Image/logo.png")
image = image.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
imagelabel = Label(
    window,
    image=img, bg="#ffe599"
)
imagelabel.place(x=1150, y=25)

# Création menu déroulant
variable = StringVar(window)
variable.set(OptionList[0])

opt = OptionMenu(window, variable, *OptionList)
opt.config(width=15, font=('Helvetica', 10))
opt.place(x=45, y=90, width=300)

label = Label(text="Liste of commands : ", bg="#ffe599")
label.place(x=30, y=55)
label.config(padx=0)

button = Button(text="Print", command=choix_action)
button.place(x=45, y=150, width=125)

# Lancement de l'interface graphique
window.mainloop()

# vider la memoire cache
files = os.listdir("./ImageGen")
for i in range(0, len(files)):
    os.remove('./ImageGen'+'/'+files[i])
