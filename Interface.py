from tkinter import *
import sqlite3

window = Tk()
window.geometry("1920x1080")

label = Label(text="Liste of commands : ")
label.place(x=30, y=30)
label.config(padx=0)

label1 = Label(text="1. Print PIB of countries where you are")
label1.place(x=45, y=50)
label1.config(padx=0)

label2 = Label(text="2. Print emissions of countries where you are")
label2.place(x=45, y=70)
label.config(padx=0)


window.mainloop()