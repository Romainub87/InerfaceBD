from lib2to3.pgen2.token import LEFTSHIFT
import os
from re import match
from tkinter import *
import sqlite3
from tkinter.font import BOLD
from turtle import bgcolor, color, onclick, onkeypress, onscreenclick, pos, position
from xmlrpc.client import boolean
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ConvertImage import convertImage
from os import listdir
from os.path import isfile, join
from CreaImage import *


def menu(display):
    menubar = Menu(display)
    menubar.add_cascade(label="Home", command=window)
    menubar.add_cascade(label="C'est quoi l'empreinte carbone ?",
                        command=openDisplayProblematique)
    menubar.add_cascade(
        label="Nos impacts sur l'environnement", command=openDisplayImpact)
    menubar.add_cascade(label="Carte du monde", command=openDisplayMap)
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
                  bg="#ffe599", font=("FARRAY", 25))
    title.pack()
    title.config(padx=0)

    lab1 = Label(displayImpact, text="Pays où vous êtes",
                 bg="#ffe599", font=("Segoe UI Semibold", 12))
    lab1.place(x=30, y=100)
    lab1.config(padx=0)

    def openChart(var):
        match var:
            case 1 : print("oui")
            case 2 : print("non")
            case 3 : print("non")
            case 4 : print("non")
            case 5 : print("non")
            case 6 : print("non")
            case 7 : print("non")

    ###BUTTONS PAYS###
    bu1 = Button(displayImpact, text="France", command=lambda *args: openChart(1), bg="#03224c", fg="white")
    bu1.place(x=70, y=150, width=200, height=20)
    bu2 = Button(displayImpact, text="Allemagne",
                 command=lambda *args: openChart(2), bg="#000000", fg="white")
    bu2.place(x=70, y=190, width=200, height=20)
    bu3 = Button(displayImpact, text="Inde",
                 command=lambda *args: openChart(3), bg="#FF9933", fg="white")
    bu3.place(x=70, y=220, width=200, height=20)
    bu4 = Button(displayImpact, text="Chine",
                 command=lambda *args: openChart(4), bg="#DE9210", fg="white")
    bu4.place(x=70, y=250, width=200, height=20)
    bu5 = Button(displayImpact, text="Etats-Unis",
                 command=lambda *args: openChart(5), bg="#3C3B6E", fg="white")
    bu5.place(x=70, y=280, width=200, height=20)
    bu6 = Button(displayImpact, text="Danemark",                
                 command=lambda *args: openChart(6), bg="#D1050C", fg="white")
    bu6.place(x=70, y=310, width=200, height=20)
    bu7 = Button(displayImpact, text="Côte d'Ivoire",
                 command=lambda *args: openChart(7), bg="#F77D0D", fg="white")
    bu7.place(x=70, y=340, width=200, height=20)
    
    
    
    labelAction = Label(displayImpact, image=None, bg="#ffe599")
    labelAction.place(x=290, y=150, width=800, height=500)
    image5 = Image.open(convertImage("Image/logo.png"))
    image5 = image5.resize((200, 200), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(image5)
    labelGraph = Label(
        displayImpact,
        image=img5, bg="#ffe599"
    )
    labelGraph.place(x=1150, y=25)

    imageChart = Label(
        displayImpact, image=imgChart, bg="#ffe599"
    )
    imageChart.place(x=550, y=50)

    legende1 = Label(displayImpact, text="Pollution au niveau mondial de vos activités",
                     bg="#ffe599", font=("Segoe UI", 12))
    legende1.place(x=550, y=620)

    graphe = Label(
        displayImpact, image=imgExemple, bg="#ffe599"
    )
    graphe.place(x=600, y=430)

    lab2 = Label(displayImpact, text="Pollution de l'activité au niveau du pays",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab2.place(x=565, y=350)
    

    


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

    image4 = Image.open(convertImage("Image/logo.png"))
    image4 = image4.resize((200, 200), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(image4)
    labelGraph = Label(
        displayProblematique,
        image=img4, bg="#ffe599"
    )
    labelGraph.place(x=1150, y=25)

    Illus = Label(displayProblematique, image=imgMamie, bg="#ffe599")
    Illus.place(x=250, y=410)

    bu = Button(displayProblematique, text="Découvrir les solutions possibles",
                command=openDisplaySolution, bg="#11ff11")
    bu.place(x=1125, y=620, width=200, height=25)


def openDisplaySolution():
    displayMap = Toplevel(window)
    displayMap.configure(bg="#ffe599")
    displayMap.minsize(width=1400, height=700)
    displayMap.maxsize(width=1400, height=700)
    displayMap.iconbitmap('Image/logo.ico')
    displayMap.title('SensiClimax - CafésPierre/Problematique/Solution')
    menu(displayMap)

    lab1 = Label(displayMap, text="Solution pour limiter l'empreinte carbone :",
                 bg="#ffe599", font=("Segoe UI Semibold", 12))
    lab1.place(x=30, y=100)
    lab1.config(padx=0)

    lab2 = Label(displayMap, text="- Changer de méthode de culture : Utiliser avec parcimoinie les pesticides, arrêter la monoculture",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab2.place(x=30, y=150)
    lab2.config(padx=0)

    lab3 = Label(displayMap, text="- Changer de gamme de produit : Proposer une nouvelle gamme plus responsable mais plus coûteux comme le café d'épeautre, sarrasin torréfié ",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab3.place(x=30, y=210)
    lab3.config(padx=0)

    lab4 = Label(displayMap, text="- Proposer des filières dit responsable pour accompagner la production du café",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab4.place(x=30, y=260)
    lab4.config(padx=0)

    image3 = Image.open(convertImage("Image/logo.png"))
    image3 = image3.resize((200, 200), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(image3)
    labelGraph = Label(
        displayMap,
        image=img3, bg="#ffe599"
    )
    labelGraph.place(x=1150, y=25)

def donothing():
    pass


def openDisplayMap():
    displayMap = Toplevel(window)
    displayMap.configure(bg="#ffe599")
    displayMap.minsize(width=1400, height=700)
    displayMap.maxsize(width=1400, height=700)
    displayMap.iconbitmap('Image/logo.ico')
    displayMap.title('SensiClimax - CafésPierre/Map')
    menu(displayMap)

    title = Label(displayMap, text="Carte du monde",
                  bg="#ffe599", font=("FARRAY", 25))
    title.pack()
    title.config(padx=0)

    labPollution = Label(displayMap,
                         bg="#ffe599", font=("Segoe UI Semibold", 10))
    labPollution.place(x=600, y=350)

    labGraphe = Label(displayMap, bg="#ffe599")
    labGraphe.place(x=0, y=445)

    labMap = Label(displayMap, bg="#ffe599")
    labMap.place(x=450, y=125)

    imgG = Image.open(
        "./Image/graphe.png").resize((350, 250), Image.ANTIALIAS)
    imgGraph = ImageTk.PhotoImage(imgG)

    imgD = Image.open(
        "./Image/graphique.png").resize((350, 250), Image.ANTIALIAS)
    imgDG = ImageTk.PhotoImage(imgD)

    map = PhotoImage(file=convertImage("ImageGen/figure.png"))

    pie = PhotoImage(file="Image/modele.png")

    def isClick():

        # Aucun sélectionné
        if ((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Aucun sélectionné")
            labGraphe.config(image=None)
        # 1 sélectionné
        elif ((var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Pollution")
            labGraphe.config(image=imgGraph)
            labMap.config(image=img)
        elif((var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Niveau de la mer")
            labGraphe.config(image=imgDG)
            labMap.config(image=map)
        elif((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0)):
            labPollution.config(text="Nb d'habitant")
            labMap.config(image=pie)
        elif((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1)):
            labPollution.config(text="PIB")
            labGraphe.config(image=None)

        # 2 sélectionnés
        elif((var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Pollution/ Niveau de la mer")
            labGraphe.config(image=None)
        elif((var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0)):
            labPollution.config(text="Pollution/ Nb d'habitant")
            labGraphe.config(image=None)
        elif((var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1)):
            labPollution.config(text="Pollution / PIB")
            labGraphe.config(image=None)
        elif((var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 0)):
            labPollution.config(text="Niveau de la mer / Nb d'habitant")
            labGraphe.config(image=None)
        elif((var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 1)):
            labPollution.config(text="Niveau de la mer / PIB")
            labGraphe.config(image=None)
        elif((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & var4.get() == 1):
            labPollution.config(text="Nb d'habitant / PIB")
            labGraphe.config(image=None)

        # 3 sélectionnés
        elif((var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 0)):
            labPollution.config(
                text="Pollution / Niveau de la mer / Nb d'habitant")
            labGraphe.config(image=None)
        elif((var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 1)):
            labPollution.config(text="Pollution / Niveau de la mer / PIB")
            labGraphe.config(image=None)
        elif(var1.get() == 0) & (var2.get() == 1 & (var3.get() == 1) & (var4.get() == 1)):
            labPollution.config(text="Niveau de la mer / Nb d'habitant / PIB")
            labGraphe.config(image=None)
        elif((var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 1)):
            labPollution.config(text="Pollution / Nb d'habitant / PIB")
            labGraphe.config(image=None)

        # Tous sélectionnés
        elif((var1.get() == 1) & (var2.get() == 1) & (var3.get() == 1) & (var4.get() == 1)):
            labPollution.config(text="Tous sélectionnés")
            labGraphe.config(image=None)

    lab1 = Label(displayMap, text="Choisissez votre valeur de mesure ( plusieurs choix possibles): ",
                 bg="#ffe599", font=("Segoe UI Semibold", 10))
    lab1.place(x=30, y=130)
    lab1.config(padx=0)

    image2 = Image.open(convertImage("Image/logo.png"))
    image2 = image2.resize((200, 200), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image2)
    labelGraph = Label(
        displayMap,
        image=img2, bg="#ffe599"
    )
    labelGraph.place(x=1150, y=25)

    ##radioButton##
    var1 = IntVar()
    var1.set(0)
    R1 = Checkbutton(displayMap, text="Pollution", variable=var1,
                     onvalue=1, offvalue=0, command=isClick, bg="#ffe599")
    R1.place(x=30, y=180)

    var2 = IntVar()
    var2.set(0)
    R2 = Checkbutton(displayMap, text="Niveau de la mer",
                     variable=var2, onvalue=1, offvalue=0, command=isClick, bg="#ffe599")
    R2.place(x=30, y=210)

    var3 = IntVar()
    var3.set(0)
    R3 = Checkbutton(displayMap, text="Nombre d'habitants",
                     variable=var3, onvalue=1, offvalue=0, command=isClick, bg="#ffe599")
    R3.place(x=30, y=240)

    var4 = IntVar()
    var4.set(0)
    R4 = Checkbutton(displayMap, text="PIB", variable=var4,
                     onvalue=1, offvalue=0, command=isClick, bg="#ffe599")
    R4.place(x=30, y=270)

# Init1isation de l'interface Tkinter

if (len(os.listdir("./ImageGen")) == 0):
    CreationImage()

elif (len(os.listdir("./ImageGen")) > 0):
    window = Tk()
    window.minsize(width=1400, height=700)
    window.maxsize(width=1400, height=700)
    window.configure(bg="#ffe599")
    window.iconbitmap('Image/logo.ico')
    window.geometry("1920x1080")
    window.title('SensiClimax - CafésPierre')

    '''Récupération des images des graphiques qui seront utilisés'''
    # planisfère

    # graphique type camembert

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
    title = Label(text="Bienvenue", bg="#ffe599", fg="Black",
                  font=("FARRAY", 40))  # setting up the labels
    title.pack()

    menu(window)
    # Création du contenu de la fenêtre
    labelAction = Label(window, image=None, bg="#ffe599")
    labelAction.place(x=290, y=150, width=800, height=500)
    image = Image.open("Image/logo.png")
    image = image.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    imagelabel = Label(
        window,
        image=img, bg="#ffe599"
    )
    imagelabel.place(x=480, y=75)

    credit = Image.open("Image/logo.png")
    credit = credit.resize((200, 200), Image.ANTIALIAS)
    imgCredit = ImageTk.PhotoImage(image)

    label1 = Label(text="Le but de cette application est de comprendre les enjeux que représente nos activités a travers le monde",
                   bg="#ffe599", font=("Segoe UI Semibold", 12))
    label1.place(x=330, y=550)
    label1.config(padx=0)

    button = Button(text="Découvrir", command=donothing,
                    bg="#16B84E", fg="White")
    button.place(x=640, y=600, width=125)

    # Lancement de l'interface graphique

    window.mainloop()

    # vider la memoire cache
    if (window.destroy):
        files = os.listdir("./ImageGen")
        for i in range(0, len(files)):
            os.remove('./ImageGen'+'/'+files[i])
