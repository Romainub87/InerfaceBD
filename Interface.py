from lib2to3.pgen2.token import LEFTSHIFT
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

# Permet de savoir quelle action veut l'utilisateur


def choix_action():
    choix = int(choice.get())
    choice.delete(0)
    match choix:
        case 1:
            Action1()
        case 2:
            Action2()

# Permet de réaliser l'action 1


def Action1():
    labelAction.config(image=img3)

# Permet de réaliser l'action 1


def Action2():
    labelAction.config(image=img2)



# Initialisation de l'interface Tkinter
window = Tk()
window.minsize(width=1500, height=900)
window.maxsize(width=1500, height=900)
window.configure(bg="#ffe599")
window.iconbitmap('Image/logo.ico')
window.geometry("1920x1080")
window.title('SensiClimax - CafésPierre')

# Récupération des images des graphiques qui seront utilisés
img2 = PhotoImage(file=convertImage())
img3 = PhotoImage(file="Image/modele.png")

# Titre de la fenêtre
my_label = Label(text="Bienvenue", bg="#ffe599", fg="Black",
                 font=("FARRAY", 40))  # setting up the labels
my_label.pack()

# Création de la MenuBar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", command=None)
menubar.add_cascade(
    label="C'est quoi l'empreinte carbone ?", command=None)
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


label = Label(text="Liste of commands : ")
label.place(x=30, y=55)
label.config(padx=0)

label1 = Label(text="1. Map of the World")
label1.place(x=45, y=70)
label1.config(padx=0)

label2 = Label(text="2. Area repartition in Nouvelle-Aquitaine (percentage)")
label2.place(x=45, y=90)
label2.config(padx=0)

choice = Entry(text="")
choice.place(x=45, y=120)

button = Button(text="Print", command=choix_action)
button.place(x=45, y=150, width=125)

# Lancement de l'interface graphique
window.mainloop()
