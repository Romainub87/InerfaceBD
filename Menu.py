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
from Solution import *
from Problm import *

def menu(display):
    menubar = Menu(display)
    menubar.add_cascade(label="Home", command=window)
    menubar.add_cascade(label="C'est quoi l'empreinte carbone ?",
                        command=openDisplayProblematique)
    menubar.add_cascade(label="Nos impacts sur l'environnement", command=None)
    menubar.add_cascade(label="Carte du monde", command=None)
    menubar.add_cascade(label="Quitter", command=display.quit)
    display.config(menu=menubar)