import sqlite3
from turtle import color
import matplotlib.pyplot as plt

db = sqlite3.connect("base.sqlite")
cursor = db.cursor()

'''
utilisé pour créer un graphe reloc='upper leftprésentant une évolution,  les données renvoyées doivent correspondre à 1.nom,2.valeurx,3.valeury
'''

def plot_base_evolution(table, xname, yname,country=""):  # name of element, x_value,y_value
    xs = []
    ys = []
    name = table[0][0]
    oldname = name
    for i in range(len(table)):
        name = table[i][0]
        if (name != oldname):
            print(ys)
            plt.plot(xs, ys, label=oldname)
            oldname = name
            xs.clear()
            ys.clear()
        xs.append(table[i][1])
        if isinstance(table[i][2],str):
            ys.append(float(table[i][2].replace(",",".")))
        else:
            ys.append(table[i][2])
    plt.title(country)
    plt.plot(xs, ys, label=name)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend(loc=2, bbox_to_anchor=(1, 1), shadow=False)
    plt.tight_layout()



def plot_base_on_year(table, ylabel):
    xs = []
    ys = []
    name = table[0][0]
    oldname = name
    for i in range(len(table)):
        xs.append(table[i][0])
        ys.append(table[i][1])
    plt.figure(figsize=(13, 7))
    plt.ylabel(ylabel)
    plt.bar(xs, ys)
 



def piechart_base_on_year(table,title):
    xs = []
    ys = []
    name = table[0][0]
    oldname = name
    plt.figure(figsize=(10, 5))
    for i in range(len(table)):
        xs.append(table[i][0])
        ys.append(table[i][1])
    plt.title(title)
    plt.pie(ys, startangle=90)
    plt.axis = ("equal")
    plt.legend(xs, bbox_to_anchor=(1, 1))



def get_ressource_for_one_country(table, country):
    print(country)
    list = [i for i in table if i[3] == country]
    return list
