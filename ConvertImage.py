from fileinput import filename
from lib2to3.pgen2.token import LEFTSHIFT
from re import match
from tkinter import *
import sqlite3
from tkinter.font import BOLD
from turtle import bgcolor, pos, position
import uuid
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def convertImage(img): 
    filename = str(uuid.uuid4())
    img = Image.open(img) 
    img = img.convert("RGBA") 
  
    data = img.getdata() 
  
    newData = [] 
  
    for item in data: 
        if item[0] == 255 and item[1] == 255 and item[2] == 255: 
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item) 
  
    img.putdata(newData) 
    img.save("ImageGen/GEN_"+filename+".png", "PNG") 
    print("Successfully converted")
    path = "ImageGen/GEN_"+filename+".png"
    return path
    

