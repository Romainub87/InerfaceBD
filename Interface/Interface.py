from lib2to3.pgen2.token import LEFTSHIFT
import os
from re import match
from tkinter import *
from tkinter.font import BOLD
from turtle import bgcolor, color, onclick, onkeypress, onscreenclick, pos, position
from xmlrpc.client import boolean
from PIL import ImageTk, Image
from ConvertImage import convertImage
from os import listdir
from os.path import isfile, join
from CreaImage import CreationImage


def menu(display):
    menubar = Menu(display)
    menubar.add_cascade(label="Home", command=window)
    menubar.add_cascade(label="C'est quoi l'empreinte carbone ?",
                        command=openDisplayProblematique)
    menubar.add_cascade(
        label="Les impacts sur l'environnement", command=openDisplayImpact)
    menubar.add_cascade(label="Infos générales", command=openDisplayMap)
    menubar.add_cascade(label="Quitter", command=display.quit)
    display.config(menu=menubar)


def openDisplayImpact():

    displayImpact = Toplevel(window)
    displayImpact.configure(bg="#ffe599")
    displayImpact.geometry("1920x1080")
    displayImpact.minsize(width=1400, height=700)
    displayImpact.maxsize(width=1400, height=700)
    displayImpact.iconbitmap('Interface/Image/logo.ico')
    displayImpact.title('SensiClimax - CafésPierre/Impact')
    menu(displayImpact)
    title = Label(displayImpact, text="Impact des différentes activités",
                  bg="#ffe599", font=("FARRAY", 25))
    title.pack()
    title.config(padx=0)

    imgPollDan = Image.open(convertImage(
        "Interface/ImageGen/ConsoDenmark.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollDan = ImageTk.PhotoImage(imgPollDan)

    imgPollAll = Image.open(convertImage(
        "Interface/ImageGen/ConsoGermany.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollAll = ImageTk.PhotoImage(imgPollAll)

    imgPollInde = Image.open(convertImage(
        "Interface/ImageGen/ConsoIndia.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollInde = ImageTk.PhotoImage(imgPollInde)

    imgPollUsa = Image.open(convertImage(
        "Interface/ImageGen/ConsoUnited States of America.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollUsa = ImageTk.PhotoImage(imgPollUsa)

    imgPollCote = Image.open(convertImage(
        "Interface/ImageGen/ConsoIvory Coast.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollCote = ImageTk.PhotoImage(imgPollCote)

    imgPollCh = Image.open(convertImage(
        "Interface/ImageGen/ConsoChina.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollCh = ImageTk.PhotoImage(imgPollCh)

    imgPollFr = Image.open(convertImage(
        "Interface/ImageGen/ConsoFrance.png")).resize((370, 250), Image.ANTIALIAS)
    imgPollFr = ImageTk.PhotoImage(imgPollFr)

    imgRessDan = Image.open(convertImage(
        "Interface/ImageGen/EvoDenmark.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessDan = ImageTk.PhotoImage(imgRessDan)

    imgRessAll = Image.open(convertImage(
        "Interface/ImageGen/EvoGermany.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessAll = ImageTk.PhotoImage(imgRessAll)

    imgRessInde = Image.open(convertImage(
        "Interface/ImageGen/EvoIndia.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessInde = ImageTk.PhotoImage(imgRessInde)

    imgRessUsa = Image.open(convertImage(
        "Interface/ImageGen/EvoUnited States of America.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessUsa = ImageTk.PhotoImage(imgRessUsa)

    imgRessCote = Image.open(convertImage(
        "Interface/ImageGen/EvoIvory Coast.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessCote = ImageTk.PhotoImage(imgRessCote)

    imgRessCh = Image.open(convertImage(
        "Interface/ImageGen/EvoChina.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessCh = ImageTk.PhotoImage(imgRessCh)

    imgRessFr = Image.open(convertImage(
        "Interface/ImageGen/EvoFrance.png")).resize((370, 250), Image.ANTIALIAS)
    imgRessFr = ImageTk.PhotoImage(imgRessFr)

    imgPollGen = Image.open(convertImage(
        "Interface/ImageGen/EmissionPaysParActivite.png")).resize((650, 370), Image.ANTIALIAS)
    imgPollGen = ImageTk.PhotoImage(imgPollGen)

    def openChart(var):
        match var:
            case 1:
                graoheTempRess.config(image=imgRessFr)
                grapheTempPoll.config(image=imgPollFr)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")
            case 2:
                graoheTempRess.config(image=imgRessAll)
                grapheTempPoll.config(image=imgPollAll)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")
            case 3:
                graoheTempRess.config(image=imgRessInde)
                grapheTempPoll.config(image=imgPollInde)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")
            case 4:
                graoheTempRess.config(image=imgRessCh)
                grapheTempPoll.config(image=imgPollCh)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")
            case 5:
                graoheTempRess.config(image=imgRessUsa)
                grapheTempPoll.config(image=imgPollUsa)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")
            case 6:
                graoheTempRess.config(image=imgRessDan)
                grapheTempPoll.config(image=imgPollDan)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")
            case 7:
                graoheTempRess.config(image=imgRessCote)
                grapheTempPoll.config(image=imgPollCote)
                grapheFix.config(image=imgPollGen)
                labAct.config(text="Par secteur d'activité")
                labRess.config(text="Par ressource")

    ###BUTTONS PAYS###
    bu1 = Button(displayImpact, text="France",
                 command=lambda *args: openChart(1), bg="green", fg="white")
    bu1.place(x=70, y=160, width=250, height=20)
    bu2 = Button(displayImpact, text="Allemagne",
                 command=lambda *args: openChart(2), bg="#D1050C", fg="white")
    bu2.place(x=70, y=190, width=250, height=20)
    bu3 = Button(displayImpact, text="Inde",
                 command=lambda *args: openChart(3), bg="#9900FF", fg="white")
    bu3.place(x=70, y=220, width=250, height=20)
    bu4 = Button(displayImpact, text="Chine",
                 command=lambda *args: openChart(4), bg="#0077FF", fg="white")
    bu4.place(x=70, y=250, width=250, height=20)
    bu5 = Button(displayImpact, text="Etats-Unis",
                 command=lambda *args: openChart(5), bg="#ff4499", fg="white")
    bu5.place(x=70, y=280, width=250, height=20)
    bu6 = Button(displayImpact, text="Danemark",
                 command=lambda *args: openChart(6), bg="orange", fg="white")
    bu6.place(x=70, y=310, width=250, height=20)
    bu7 = Button(displayImpact, text="Côte d'Ivoire",
                 command=lambda *args: openChart(7), bg="brown", fg="white")
    bu7.place(x=70, y=340, width=250, height=20)

    logoAvt = Image.open(convertImage("Interface/Image/logo.png"))
    logoAvt = logoAvt.resize((250, 250), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logoAvt)

    labelLogo = Label(
        displayImpact,
        image=logo, bg="#ffe599"
    )
    labelLogo.place(x=1150, y=25)

    graoheTempRess = Label(
        displayImpact, bg="#ffe599"
    )
    graoheTempRess.place(x=750, y=75)

    grapheTempPoll = Label(
        displayImpact, bg="#ffe599"
    )
    grapheTempPoll.place(x=350, y=75)

    grapheFix = Label(
        displayImpact, image=imgPollGen, bg="#ffe599")

    grapheFix.place(x=370, y=320)

    lab1 = Label(displayImpact, text="Pays où vous êtes : ",
                 bg="#ffe599", font=("Segoe UI Semibold", 12))
    lab1.place(x=30, y=120)
    lab1.config(padx=0)

    labAct = Label(displayImpact, text="",
                 bg="#ffe599", font=("Segoe UI Semibold", 8))
    labAct.place(x=490, y=60)
    labAct.config(padx=0)
    
    labRess = Label(displayImpact, text="",
                 bg="#ffe599", font=("Segoe UI Semibold", 8))
    labRess.place(x=920, y=60)
    labRess.config(padx=0)
    

    legende1 = Label(displayImpact, text="Pollution des pays où vos usines sont implantés\n comparé entre eux",
                     bg="#ffe599", font=("Segoe UI", 12))
    legende1.place(x=540, y=650)

    lab2 = Label(displayImpact, text="Origines de la pollution au niveau du pays",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab2.place(x=550, y=332)
    lab2.config(padx=0)


def openDisplayProblematique():
    displayProblematique = Toplevel(window)
    displayProblematique.configure(bg="#ffe599")
    displayProblematique.geometry("1920x1080")
    displayProblematique.minsize(width=1400, height=700)
    displayProblematique.maxsize(width=1400, height=700)
    displayProblematique.iconbitmap('Interface/Image/logo.ico')
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

    labAct = Label(displayProblematique, text="Mettant en péril les sols tropicaux par sa méthode de monoculture, ou encore la déforestation sans compter le transport du café depuis le pays de production. ", bg="#ffe599", font=("Segoe UI", 12))
    labAct.place(x=30, y=200)
    labAct.config(padx=0)

    lab4 = Label(displayProblematique, text="Son empreinte est 4,98 kg de CO2 avant torréfaction.",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab4.place(x=30, y=250)
    lab4.config(padx=0)

    lab5 = Label(displayProblematique, text="Le saviez vous ?",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab5.place(x=30, y=300)
    lab5.config(padx=0)

    lab6 = Label(displayProblematique, text="Les français, consommateur n°1 de café en capsule, il consitue un facteur important de pollution par sa présence de plastique et lab1luminium et sa diffculté a recycler.",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab6.place(x=30, y=350)
    lab6.config(padx=0)

    image4 = Image.open(convertImage("./Interface/Image/logo.png"))
    image4 = image4.resize((250, 250), Image.ANTIALIAS)
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
    bu.place(x=1125, y=620, width=250, height=25)


def openDisplaySolution():
    displayMap = Toplevel(window)
    displayMap.configure(bg="#ffe599")
    displayMap.minsize(width=1400, height=700)
    displayMap.maxsize(width=1400, height=700)
    displayMap.iconbitmap('./Interface/Image/logo.ico')
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

    labAct = Label(displayMap, text="- Changer de gamme de produit : Proposer une nouvelle gamme plus responsable mais plus coûteux comme le café d'épeautre, sarrasin torréfié ",
                 bg="#ffe599", font=("Segoe UI", 12))
    labAct.place(x=30, y=200)
    labAct.config(padx=0)

    lab4 = Label(displayMap, text="- Proposer des filières dit responsable pour accompagner la production du café",
                 bg="#ffe599", font=("Segoe UI", 12))
    lab4.place(x=30, y=250)
    lab4.config(padx=0)

    logoAvt = Image.open(convertImage("Interface/Image/logo.png"))
    logoAvt = logoAvt.resize((250, 250), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logoAvt)
    labelGraph = Label(
        displayMap,
        image=logo, bg="#ffe599"
    )
    labelGraph.place(x=1150, y=25)


def donothing():
    pass


def openDisplayMap():
    displayMap = Toplevel(window)
    displayMap.configure(bg="#ffe599")
    displayMap.minsize(width=1400, height=700)
    displayMap.maxsize(width=1400, height=700)
    displayMap.iconbitmap('Interface/Image/logo.ico')
    displayMap.title('SensiClimax - CafésPierre/Map')
    menu(displayMap)

    title = Label(displayMap, text="Infos générales",
                  bg="#ffe599", font=("FARRAY", 25))
    title.pack()
    title.config(padx=0)

    labPollution = Label(displayMap,
                         bg="#ffe599", font=("Segoe UI Semibold", 20))
    labPollution.pack()

    labGraphe = Label(displayMap, bg="#ffe599")
    labGraphe.place(x=0, y=445)

    labMap = Label(displayMap, bg="#ffe599")
    labMap.place(x=450, y=125)
    
    grPoll = Image.open(convertImage("Interface/ImageGen/Emission30ans.png")).resize((400, 250), Image.ANTIALIAS)
    grPoll = ImageTk.PhotoImage(grPoll)
    
    grPibHab = Image.open(convertImage("Interface/ImageGen/PIB.Hab.png")).resize((650, 400), Image.ANTIALIAS)
    grPibHab = ImageTk.PhotoImage(grPibHab)
    
    grHab = Image.open(convertImage("Interface/ImageGen/Population.png")).resize((650, 400), Image.ANTIALIAS)
    grHab = ImageTk.PhotoImage(grHab)
    
    grPib = Image.open(convertImage("Interface/ImageGen/PIB.png")).resize((650, 400), Image.ANTIALIAS)
    grPib = ImageTk.PhotoImage(grPib)

    def isClick():

        # Aucun sélectionné
        if ((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Aucun sélectionné")
            labGraphe.config(image="")
            labMap.config(image="")
        # 1 sélectionné
        elif ((var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Pollution")
            labGraphe.config(image=grPoll)
            labMap.config(image="")
        elif((var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0)):
            labPollution.config(text="Niveau de la mer")
            labGraphe.config(image="")
            labMap.config(image="")
        elif((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0)):
            labPollution.config(text="Nb Habitants")
            labGraphe.config(image="")
            labMap.config(image=grHab)
        elif((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1)):
            labPollution.config(text="PIB")
            labGraphe.config(image="")
            labMap.config(image=grPib)
        elif((var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 1)):
            labPollution.config(text="PIB/Nb d'habitant")
            labGraphe.config(image="")
            labMap.config(image=grPibHab)
        else:
            labPollution.config(text="Données imcompatibles")
            labGraphe.config(image="")
            labMap.config(image="")

    lab1 = Label(displayMap, text="Choisissez votre valeur de mesure (plusieurs choix possibles): ",
                 bg="#ffe599", font=("Segoe UI Semibold", 10))
    lab1.place(x=30, y=130)
    lab1.config(padx=0)

    image2 = Image.open(convertImage("./Interface/Image/logo.png"))
    image2 = image2.resize((250, 250), Image.ANTIALIAS)
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


if (len(os.listdir("./Interface/ImageGen/")) == 0):
    CreationImage()
    print("Vos images ont été généré, veuillez démarrer l'application")
elif (len(os.listdir("./Interface/ImageGen/")) > 0):
    window = Tk()
    window.minsize(width=1400, height=700)
    window.maxsize(width=1400, height=700)
    window.configure(bg="#ffe599")
    window.iconbitmap('./Interface/Image/logo.ico')
    window.geometry("1920x1080")
    window.title('SensiClimax - CafésPierre')

    '''Récupération des images des graphiques qui seront utilisés'''
    # planisfère

    # graphique type camembert

    mamie = Image.open("./Interface/Image/Mamie.png")
    mamie = mamie.resize((430, 270), Image.ANTIALIAS)
    imgMamie = ImageTk.PhotoImage(mamie)

    # Titre de la fenêtre
    title = Label(text="Bienvenue", bg="#ffe599", fg="Black",
                  font=("FARRAY", 40))  # setting up the labels
    title.pack()

    menu(window)
    # Création du contenu de la fenêtre
    labelAction = Label(window, image=None, bg="#ffe599")
    labelAction.place(x=290, y=250, width=800, height=500)
    image = Image.open("Interface/Image/logo.png")
    image = image.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    imagelabel = Label(
        window,
        image=img, bg="#ffe599"
    )
    imagelabel.place(x=480, y=75)

    credit = Image.open("Interface/Image/logo.png")
    credit = credit.resize((250, 250), Image.ANTIALIAS)
    imgCredit = ImageTk.PhotoImage(image)

    label1 = Label(text="Le but de cette application est de comprendre les enjeux que représente nos activités a travers le monde",
                   bg="#ffe599", font=("Segoe UI Semibold", 12))
    label1.place(x=330, y=550)
    label1.config(padx=0)

    button = Button(text="Découvrir", command=openDisplayMap,
                    bg="#16B84E", fg="White")
    button.place(x=640, y=600, width=125)

    # Lancement de l'interface graphique

    window.mainloop()

    # vider la memoire cache
    if (window.destroy):
        files = os.listdir("./Interface/ImageGen")
        for i in range(0, len(files)):
            os.remove('./Interface/ImageGen'+'/'+files[i])
