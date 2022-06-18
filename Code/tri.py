import sqlite3
from glob import iglob

import numpy as np
import pandas as pd
from math import isnan
import netCDF4 as nc
import xarray as xr
from numpy import int64

db = sqlite3.connect("base.sqlite")
cursor = db.cursor()
countries_continent = {"France": "Europe", "Ivory Coast": "Africa", "United States of America": "North America",
                       "Germany": "Europe", "India": "Asia and Oceania", "China": "Asia and Oceania",
                       "Denmark": "Europe"}
fossilFuel = ["Oil", "Coal", "Gas", "Fuel Ethanol"]


def insert_continent():
    cursor.execute("""INSERT OR IGNORE INTO CONTINENT(nom) VALUES
    ("Europe"),
    ("Asia and Oceania"),
    ("North America"),
    ("Central and South America"),
    ("Africa")""")
    db.commit()


def insert_countries():
    for pathname in iglob("./Fichier essentiels/Greenhouse Gas by sector*"):
        cursor.execute("""SELECT idContinent FROM Continent WHERE nom=(?)""", (
            (countries_continent.get(pathname.split(",")[1].strip()),)))
        continent = cursor.fetchone()
        cursor.execute("""INSERT OR IGNORE INTO PAYS(nom,Continent) VALUES(?,?)""", ((pathname.split(",")[1].strip()),
                                                                                     continent[0]))
    db.commit()


def insert_activities_type():
    csv_to_insert = pd.read_csv("./Fichier essentiels/Greenhouse Gas by sector, China, 1850-2016 (in MtCO2eq).csv",
                                delimiter=";")
    for i in range(1, len(csv_to_insert.columns)):
        cursor.execute("""INSERT OR IGNORE INTO ActiviteType(nom) VALUES(?)""", (csv_to_insert.columns[i],))
    csv_to_insert = pd.read_csv("./Fichier essentiels/Final Energy by sector, China, 1990-2015 (in Mtoe).csv",
                                delimiter=";")
    for i in range(1, len(csv_to_insert.columns)):
        cursor.execute("""INSERT OR IGNORE INTO ActiviteType(nom) VALUES(?)""", (csv_to_insert.columns[i],))
    db.commit()


def insert_country_activities(typeEmission):
    if typeEmission == "ghs":
        path = "./Fichier essentiels/Greenhouse Gas by sector*"
    elif typeEmission == "énergétique":
        path = "./Fichier essentiels/Final Energy by sector*"
    else:
        return 0
    for pathname in iglob(path):
        country = pathname.split(",")[1].strip()
        cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", (country,))
        country_id = cursor.fetchone()[0]
        df_country = pd.read_csv(pathname, delimiter=";")
        df_country = df_country[(df_country[df_country.columns[0]] > "1986-01-01")]
        df_country.index = pd.RangeIndex(start=0, stop=len(df_country), step=1)
        for types in range(1, len(df_country.columns)):
            cursor.execute("""SELECT idActiviteType FROM ActiviteType WHERE nom=(?)""", (df_country.columns[types],))
            id_activite_type = cursor.fetchone()[0]
            for i in range(1, len(df_country)):
                year = int(df_country[df_country.columns[0]][i][0:4])
                if typeEmission == "ghs":
                    cursor.execute(
                    """INSERT OR IGNORE INTO EmissionPays(quantiteMC02eq,annee,paysProducteur,typeActivite)
                     VALUES(?,?,?,?)""", (df_country[df_country.columns[types]][i], year, country_id, id_activite_type,))
                elif typeEmission == "énergétique":
                    cursor.execute("""INSERT OR IGNORE INTO EnergieConsommeePays(quantiteMtoe,annee,paysProducteur,typeActivite)
                    VALUES (?,?,?,?)""",(df_country[df_country.columns[types]][i], year, country_id, id_activite_type,))

    db.commit()


def insert_continent_activities():
    df_continent = pd.read_csv("./Fichier essentiels/Greenhouse Gas, 1850-2016 (in MtCO2eq).csv", delimiter=";")
    df_continent = df_continent[(df_continent[df_continent.columns[0]] >= "1986-01-01")]
    df_continent.index = pd.RangeIndex(start=0, stop=len(df_continent), step=1)
    for continent in range(1, len(df_continent.columns)):
        cursor.execute("""SELECT idContinent FROM Continent WHERE nom=(?)""", (df_continent.columns[continent],))
        continent_id = cursor.fetchone()
        for i in range(1, len(df_continent)):
            year = int(df_continent[df_continent.columns[0]][i][0:4])
            cursor.execute("""INSERT OR IGNORE INTO ActiviteContinentale(quantiteEmission,annee,continentProducteur)
             VALUES(?,?,?)""", (df_continent[df_continent.columns[continent]][i], year, continent_id[0]))
    db.commit()


def insert_ressources_type():
    ressource_type_csv = pd.read_csv(
        "./Fichier essentiels/Primary Energy Production by source, France, 1900-2016 (in Mtoe).csv",
        delimiter=";")
    for i in range(1, len(ressource_type_csv.columns)):
        cursor.execute("""INSERT OR IGNORE INTO RessourceType(nom) VALUES(?)""", (ressource_type_csv.columns[i],))
    ressource_type_csv = pd.read_csv("./Fichier essentiels/Final Energy by source, China, 1971-2015 (in Mtoe).csv",delimiter=";")
    for i in range(1, len(ressource_type_csv.columns)):
        cursor.execute("""INSERT OR IGNORE INTO RessourceType(nom) VALUES(?)""", (ressource_type_csv.columns[i],))
    db.commit()


def insert_ressources(typeEmission):
    if typeEmission == "produite" or typeEmission == "Produite":
        path = "./Fichier essentiels/Primary Energy Production by source*"
        type_of_emission = "produite"
    elif typeEmission == "consomee" or typeEmission == "Consomee":
        path = "./Fichier essentiels/Primary Energy Consumption by source*"
        type_of_emission = "consomee"
    elif typeEmission == "consomeeFin" or typeEmission == "ConsomeeFin":
        path = "./Fichier essentiels/Final Energy by source*"
        type_of_emission = "consomeeFin"
    else:
        return 0
    for pathname in iglob(path):
        country = pathname.split(",")[1].strip()
        cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", (country,))
        country_id = cursor.fetchone()[0]
        df_country = pd.read_csv(pathname, delimiter=";")
        df_country = df_country[(df_country[df_country.columns[0]] > "1986-01-01")]
        df_country.index = pd.RangeIndex(start=0, stop=len(df_country), step=1)
        for types in range(1, len(df_country.columns)):
            isFossil = df_country.columns[types] in fossilFuel
            cursor.execute("""SELECT idType FROM RessourceType WHERE nom=(?)""", (df_country.columns[types],))
            id_activite_type = cursor.fetchone()[0]
            for i in range(1, len(df_country)):
                value = df_country[df_country.columns[types]][i]
                type_of_value = type(value)
                year = int(df_country[df_country.columns[0]][i][0:4])
                if not isinstance(df_country[df_country.columns[types]][i], float) and \
                        df_country[df_country.columns[types]][i] != "0" and df_country[df_country.columns[types]][i] \
                        is not None and not isinstance(df_country[df_country.columns[types]][i],int64):
                    cursor.execute("""INSERT INTO Ressource(quantiteEmission,estFossile,produitPar,annee,typeRessource,typeProduction) 
                    VALUES(?,?,?,?,?,?)""", (
                        df_country[df_country.columns[types]][i], isFossil, country_id, year, id_activite_type,type_of_emission,))
    cursor.execute("""DELETE FROM Ressource WHERE quantiteEmission=(?)""",("0x0000000000000000",))
    db.commit()



def insert_pib():
    df_pib = pd.read_csv("./Fichier essentiels/API_NY.GDP.MKTP.KD_DS2_en_excel_v2_4150998.csv", delimiter=";")
    cursor.execute("""SELECT nom FROM Pays""")
    list_of_countries = cursor.fetchall()
    list_of_countries = [i[0] for i in list_of_countries]
    list_of_countries.remove("Ivory Coast")
    list_of_countries.append("Cote d'Ivoire")  # because this csv is shit
    list_of_countries.remove("United States of America")
    list_of_countries.append("United States")
    for country in list_of_countries:
        if country != "Cote d'Ivoire" and country != "United States":
            cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", (country,))
        elif country == "Cote d'Ivoire":
            cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", ("Ivory Coast",))
        elif country == "United States":
            cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", ("United States of America",))
        country_id = cursor.fetchone()[0]
        country_df = df_pib[df_pib["Country Name"] == country]
        for types in range(31, len(country_df.columns) - 5):
            isolated_value = country_df[country_df.columns[types]][country_df.index[0]]
            year = int(country_df.columns[types])
            cursor.execute("""INSERT OR IGNORE INTO PIB VALUES(?,?,?)""", (isolated_value, year, country_id))
    db.commit()
def insert_population():
    df_population = pd.read_csv("./Fichier essentiels/GM-Population - Dataset - v6.csv", delimiter=";")
    cursor.execute("""SELECT nom FROM Pays""")
    list_of_countries = cursor.fetchall()
    list_of_countries = [i[0] for i in list_of_countries]
    list_of_countries.remove("Ivory Coast")
    list_of_countries.append("Cote d'Ivoire")  # because this csv is shit
    for country in list_of_countries:
        if country != "Cote d'Ivoire":
            cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", (country,))
        else:
            cursor.execute("""SELECT idPays FROM Pays WHERE nom=(?)""", ("Ivory Coast",))
        country_id = cursor.fetchone()[0]
        country_df = df_population[df_population["name"] == country]
        country_df = country_df[187:len(country_df) - 84]
        country_df.index = pd.RangeIndex(start=0, stop=len(country_df), step=1)
        for i in range(0, len(country_df)):
            cursor.execute("""INSERT OR IGNORE INTO Population VALUES(?,?,?)""",
                           (country_id, int(country_df["time"][i]), int((country_df["Population"][i]), )))
    db.commit()

def convertNCToCSV(NCFileName,CSVFileName):
    xr.open_dataset( NCFileName).to_dataframe().to_csv("./Fichier essentiels/" + CSVFileName, ";")

def insert_sea_level():
    df_sea_level = pd.read_csv("./Fichier essentiels/seaLevelRise.csv", delimiter=";")
    for column in range(1, len(df_sea_level)):
        cursor.execute("""INSERT INTO niveauMer(longitude,latitude,niveauMer) VALUES(?,?,?)""", (
            df_sea_level[df_sea_level.columns[1]][column], df_sea_level[df_sea_level.columns[0]][column],
        df_sea_level[df_sea_level.columns[3]][column]
        ))
    db.commit()

def insert_mean_temperature():
    df_mean_temperature = pd.read_csv("./Fichier essentiels/seaLevelRise.csv", delimiter=";")
    for column in range(1, len(df_mean_temperature)):
        cursor.execute("""INSERT INTO temperature(longitude,latitude,temperature) VALUES(?,?,?)""", (
            df_mean_temperature[df_mean_temperature.columns[1]][column], df_mean_temperature[df_mean_temperature.columns[0]][column],
            df_mean_temperature[df_mean_temperature.columns[3]][column]
        ))
    db.commit()



def convertNCToCSV(NCFileName,CSVFileName):
    xr.open_dataset(NCFileName).to_dataframe().to_csv("./Fichier essentiels/" + CSVFileName, ";")

def insert_sea_level():
    df_sea_level = pd.read_csv("./Fichier essentiels/seaLevelRise.csv", delimiter=";")
    for column in range(1, len(df_sea_level)):
        if not np.isnan(df_sea_level[df_sea_level.columns[3]][column]):
            cursor.execute("""INSERT INTO niveauMer(longitude,latitude,niveauMer) VALUES(?,?,?)""", (
                df_sea_level[df_sea_level.columns[1]][column], df_sea_level[df_sea_level.columns[0]][column],
                df_sea_level[df_sea_level.columns[3]][column]))
    db.commit()

def insert_mean_temperature():
    df_mean_temperature = pd.read_csv("./Fichier essentiels/seaLevelRise.csv", delimiter=";")
    for column in range(1, len(df_mean_temperature)):
        if not np.isnan(df_mean_temperature[df_mean_temperature.columns[3]][column]):
            cursor.execute("""INSERT INTO temperature(longitude,latitude,temperature) VALUES(?,?,?)""", (
                df_mean_temperature[df_mean_temperature.columns[1]][column], df_mean_temperature[df_mean_temperature.columns[0]][column],
                df_mean_temperature[df_mean_temperature.columns[3]][column]))
    db.commit()

def insert_world_production():
    df_world = pd.read_csv("./Fichier essentiels/Greenhouse Gas, World, 1850-2016 (in MtCO2eq).csv",delimiter=";")
    df_world = df_world[(df_world[df_world.columns[0]] > "1986-01-01")]
    df_world.index = pd.RangeIndex(start=0,stop=len(df_world),step=1)
    for i in range(1,len(df_world)):
        year = df_world[df_world.columns[0]][i][0:4]
        cursor.execute("""INSERT INTO emissionsMondiales VALUES(?,?)""",(year,df_world[df_world.columns[1]][i],))
    db.commit()
convertNCToCSV("Fichier essentiels/CMIP6 - Sea level rise (SLR) Change meters - Long Term (2081-2100) SSP1-2.6 (rel. to 1995-2014) - Annual .nc","seaLevelRise.csv")
convertNCToCSV("Fichier essentiels/CMIP6 - Mean temperature (T) Change deg C - Medium Term (2041-2060) SSP5-8.5 (rel. to 1995-2014) - Annual (34 models).nc", "meanTemperature.csv")

insert_continent()
insert_countries()
insert_activities_type()
insert_country_activities("ghs")
insert_country_activities("énergétique")
insert_continent_activities()
insert_ressources_type()
insert_ressources("consomee")
insert_ressources("produite")
insert_ressources("consomeeFin")
insert_pib()
insert_population()
insert_world_production()
convertNCToCSV("Fichier essentiels/CMIP6 - Sea level rise (SLR) Change meters - Long Term (2081-2100) SSP1-2.6 (rel. to 1995-2014) - Annual .nc","seaLevelRise.csv")
convertNCToCSV("Fichier essentiels/CMIP6 - Mean temperature (T) Change deg C - Medium Term (2041-2060) SSP5-8.5 (rel. to 1995-2014) - Annual (34 models).nc", "meanTemperature.csv")
insert_sea_level()
insert_mean_temperature()
