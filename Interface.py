from enum import auto
from re import match
from tkinter import *
import sqlite3
from turtle import bgcolor, pos
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_Nouvelle_Aquitaine = [[16, 'Charente', 352015, 5956.0],
                           [17, 'Charente-Maritime', 651358, 6863.8],
                           [19, 'Corrèze', 240073, 5856.8],
                           [23, 'Creuse', 116617, 5565.4],
                           [24, 'Dordogne', 413223, 9060.0],
                           [33, 'Gironde', 1623749, 9975.6],
                           [40, 'Landes', 413690, 9242.6],
                           [47, 'Lot-et-Garonne', 331271, 5360.9],
                           [64, 'Pyrénées-Atlantiques', 682621, 7644.8],
                           [79, 'Deux-Sèvres', 374878, 5999.4],
                           [86, 'Vienne', 438435, 6990.4],
                           [87, 'Haute-Vienne', 372359, 5520.1]]

df = pd.DataFrame(data_Nouvelle_Aquitaine, columns=[
                  'Dept', 'Region', 'Pop', 'Superficie'])


def aff():
    data = data_Nouvelle_Aquitaine
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'pink', 'turquoise',
              'purple', 'orange', 'gray', 'white']
    plt.title('Pourcentages populations départements Nouvelle-Aquitaine')
    plt.pie([d[2] for d in data],
            labels=[d[1] + ' (' + str(d[0]) + ')' for d in data],
            colors=colors,
            autopct='%1.1f %%',
            shadow=False,
            startangle=90)
    plt.axis('equal')
    plt.savefig("Image/figure.png")


def choix_action():
    choix = int(choice.get())
    match choix:
        case 1:
            afficherAff()
        case 2:
            Label(image=PhotoImage(file='Image/figure.png'))


def afficherAff():
    label = Label(text="Bienvenue")
    label.place(x=300, y=50)
    label.config(padx=0)


def donothing():
    x = 0


window = Tk()
window.configure(bg="#ffe599")
window.iconbitmap('Image/logo.ico')
window.geometry("1920x1080")
window.title('SensiClimax - CafésPierre')

my_label = Label(text="Bienvenue", bg="#ffe599", fg="Black",
                 font=("Arial", 40))  # setting up the labels
my_label.pack()

# Création de la MenuBar

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", command=donothing())
menubar.add_cascade(
    label="C'est quoi l'empreinte carbone ?", command=donothing)
menubar.add_cascade(label="Nos impacts sur l'environnement", command=donothing)
menubar.add_cascade(label="Carte du monde", command=donothing)
menubar.add_cascade(label="Quitter", command=window.quit)

window.config(menu=menubar)


img = PhotoImage(file='Image/logo.png')
imagelabel = Label(
    window,
    image=img, bg="#ffe599"
)
imagelabel.place(x=1000, y=150)


label = Label(text="Liste of commands : ")
label.place(x=30, y=30)
label.config(padx=0)

label1 = Label(text="1. Print PIB of countries where you are")
label1.place(x=45, y=50)
label1.config(padx=0)

label2 = Label(text="2. Print emissions of countries where you are")
label2.place(x=45, y=70)
label.config(padx=0)

img2 = PhotoImage(file='Image/figure.png')
labelAction = Label(image=img2)
labelAction.place(x=350, y=150, width=650, height=500)
labelAction.config(padx=0)

choice = Entry(text="")
choice.place(x=45, y=100)

button = Button(text="Print", command=choix_action)
button.place(x=55, y=150)


window.mainloop()
