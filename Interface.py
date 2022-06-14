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

def menu(display):
    menubar = Menu(display)
    menubar.add_cascade(label="Home", command=window)
    menubar.add_cascade(label="C'est quoi l'empreinte carbone ?",
                        command=openDisplayProblematique)
    menubar.add_cascade(label="Nos impacts sur l'environnement", command=None)
    menubar.add_cascade(label="Carte du monde", command=None)
    menubar.add_cascade(label="Quitter", command=display.quit)
    display.config(menu=menubar)


def openDisplayImpact():
    displayImpact = Toplevel(window)
    displayImpact.configure(bg="#ffe599")
    displayImpact.geometry("1920x1080")
    displayImpact.minsize(width=1400, height=700)
    displayImpact.maxsize(width=1400, height=700)
    displayImpact.iconbitmap('Image/logo.ico')
    displayImpact.title('SensiClimax - CafésPierre/Impact')
    menu(displayImpact)
    title = Label(displayImpact, text="Impact de vos activités",
                  bg="#ffe599", font=("Segoe UI", 18))
    title.place(x=1125, y=50)
    title.config(padx=0)
    lab1 = Label(displayImpact, text="Pays où vous êtes",
                 bg="#ffe599", font=("Segoe UI Semibold", 12))
    lab1.place(x=30, y=100)
    lab1.config(padx=0)
    
    
    ###BUTTONS PAYS###
    
    bu1 = Button(displayImpact, text="France",
                command=openDisplaySolution, bg="#11ff11")
    bu1.place(x=70, y=150, width=200, height=20)
    bu2 = Button(displayImpact, text="Allemagne",
                command=openDisplaySolution, bg="#11ff11")
    bu2.place(x=70, y=190, width=200, height=20)
    bu3 = Button(displayImpact, text="Inde",
                command=openDisplaySolution, bg="#11ff11")
    bu3.place(x=70, y=220, width=200, height=20)
    bu4 = Button(displayImpact, text="Chine",
                command=openDisplaySolution, bg="#11ff11")
    bu4.place(x=70, y=250, width=200, height=20)
    bu5 = Button(displayImpact, text="Etats-Unis",
                command=openDisplaySolution, bg="#11ff11")
    bu5.place(x=70, y=280, width=200, height=20)
    bu6 = Button(displayImpact, text="Danemark",
                command=openDisplaySolution, bg="#11ff11")
    bu6.place(x=70, y=310, width=200, height=20)
    bu7 = Button(displayImpact, text="Côte d'Ivoire",
                command=openDisplaySolution, bg="#11ff11")
    bu7.place(x=70, y=340, width=200, height=20)


def openDisplayProblematique():
    
    displayProblematique = Toplevel(window)
    displayProblematique.configure(bg="#ffe599")
    displayProblematique.geometry("1920x1080")
    displayProblematique.minsize(width=1400, height=700)
    displayProblematique.maxsize(width=1400, height=700)
    displayProblematique.iconbitmap('Image/logo.ico')
    displayProblematique.title('SensiClimax - CafésPierre/Problematique')
    menu(displayProblematique)

    title = Label(displayProblematique, text="C'est quoi l'empreinte carbone ?",
                  bg="#ffe599", font=("Segoe UI", 16))
    title.place(x=30, y=50)
    title.config(padx=0)

    lab1 = Label(displayProblematique, text="- L'empreinte carbone est un indice de mesure permettant desavoir le taux de gaz a effet de serre dans le monde.",
                 bg="#ffe599", font=("Segoe UI Semibold", 12))
    lab1.place(x=30, y=100)
    lab1.config(padx=0)

    lab2 = Label(displayProblematique, text="C'est la méthode culture du café qui est a le plus d'impact écologique or pour faire face a la demande grandissante,\non a tendance aujourd'hui a préférer l'efficacité au detriment de la qulab1ité en laissant de côté les conséquences environnementlab1e. ", bg="#ffe599", font=("Segoe UI", 12))
    lab2.place(x=30, y=150)
    lab2.config(padx=0)

    lab3 = Label(displayProblematique, text="Mettant en péril les sols tropicaux par sa méthode de monoculture, ou encore la déforestation sans compter le transport du café depuis le pays de production. ", bg="#ffe599", font=("Segoe UI", 12))
    lab3.place(x=30, y=210)
    lab3.config(padx=0)

    lab4 = Label(displayProblematique, text="Son empreinte est 4,98 kg de CO2 avant torréfaction.",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab4.place(x=30, y=260)
    lab4.config(padx=0)

    lab5 = Label(displayProblematique, text="Le saviez vous ?",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab5.place(x=30, y=310)
    lab5.config(padx=0)

    lab6 = Label(displayProblematique, text="Les français, consommateur n°1 de café en capsule, il consitue un facteur important de pollution par sa présence de plastique et lab1luminium et sa diffculté a recycler.",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab6.place(x=30, y=360)
    lab6.config(padx=0)

    illustrationLabel = Label(
        displayProblematique,
        image=img, bg="#ffe599"
    )
    illustrationLabel.place(x=1150, y=25)

    mamie = PhotoImage('Image/Mamie.png')
    Illus = Label(displayProblematique, image=mamie)
    Illus.place(x=45, y=250)

    bu = Button(displayProblematique, text="Découvrir les solutions possibles",
                command=openDisplaySolution, bg="#11ff11")
    bu.place(x=1125, y=620, width=200, height=25)

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




# Initilab1isation de l'interface Tkinter
window = Tk()
window.minsize(width=1400, height=700)
window.maxsize(width=1400, height=700)
window.configure(bg="#ffe599")
window.iconbitmap('Image/logo.ico')
window.geometry("1920x1080")
window.title('SensiClimax - CafésPierre')

'''Récupération des images des graphiques qui seront utilisés'''
# planisfère
map = PhotoImage(file=convertImage())

# graphique type camembert
pie = PhotoImage(file="Image/modele.png")

# Titre de la fenêtre
my_label = Label(text="Bienvenue", bg="#ffe599", fg="Black",
                 font=("FARRAY", 40))  # setting up the labels
my_label.pack()

menu(window)

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
