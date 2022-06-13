from re import match
from tkinter import *
import sqlite3
from turtle import bgcolor, pos
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def choix_action():
    choix = int(choice.get())
    match choix:
        case 1: 
            afficherAff()
        case 2: 
            afficherNeg()

def afficherAff():
    label = Label(text="Bienvenue")
    label.place(x=300, y=50)
    label.config(padx=0)

def afficherNeg():
    label = Label(text="C'est non")
    label.place(x=300, y=50)
    label.config(padx=0)
    

window = Tk()
window.configure(bg="#ffe599") 
window.iconbitmap('Image/logo.ico')
window.geometry("1920x1080")
window.title('SensiClimax - CafésPierre')

my_label = Label(text = "Bienvenue",bg="#ffe599", fg = "Black", font = ("Arial", 40)) # setting up the labels 
my_label.pack()
 
img = PhotoImage(file='Image/logo.png')
imagelabel = Label(
    window,
    image=img,bg="#ffe599"
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

choice = Entry(text="")
choice.place(x=45, y=100)

button = Button(text="Print", command=choix_action)
button.place(x=55, y=150)



window.mainloop()

