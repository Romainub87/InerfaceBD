
from lib2to3.pgen2.token import LEFTSHIFT
from optparse import Option
import os
from re import match
from tkinter import *
import sqlite3
from tkinter.font import BOLD
from turtle import bgcolor, pos, position
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
            openNewWindow()

# Permet de d'afficher le graphe converti 

def Action1():
    labelAction.config(image=pie)

# Permet d'afficher un planisfère
def Action2():
    labelAction.config(image=map)

def openNewWindow(): 
    newWindow = Toplevel(window) 
    newWindow.title("New Window") 
    newWindow.geometry("200x200")
    newWindow.iconbitmap('Image/logo.ico')
    newWindow.title('SensiClimax - CafésPierre') 

# Initialisation de l'interface Tkinter
window = Tk()
window.minsize(width=1500, height=900)
window.maxsize(width=1500, height=900)
window.configure(bg="#ffe599")
window.iconbitmap('Image/logo.ico')
window.geometry("1920x1080")
window.title('SensiClimax - CafésPierre')

'''Récupération des images des graphiques qui seront utilisés'''
#planisfère
map = PhotoImage(file=convertImage())

#graphique type camembert
pie = PhotoImage(file="Image/modele.png")

# Titre de la fenêtre
my_label = Label(text="Bienvenue", bg="#ffe599", fg="Black", font=("FARRAY", 40))  # setting up the labels
my_label.pack()

# Création de la MenuBar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", command=None)
menubar.add_cascade(label="C'est quoi l'empreinte carbone ?", command=None)
menubar.add_cascade(label="Nos impacts sur l'environnement", command=None)
menubar.add_cascade(label="Carte du monde", command=None)
menubar.add_cascade(label="Quitter", command=window.quit)

window.config(menu=menubar)


# Création du contenu de la fenêtre
labelAction = Label(window, image=None, bg="#ffe599")
labelAction.place(x=300, y=150, width=800, height=500)

img = PhotoImage(file='Image/logo.png')
imagelabel = Label(
    window,
    image=img, bg="#ffe599"
)
imagelabel.place(x=1000, y=50)

# Création menu déroulant
variable = StringVar(window)
variable.set(OptionList[0])

opt = OptionMenu(window, variable, *OptionList)
opt.config(width=15, font=('Helvetica', 10))
opt.place(x=125, y=75, width=300)

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



