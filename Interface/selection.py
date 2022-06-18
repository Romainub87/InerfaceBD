import sqlite3

db = sqlite3.connect("base.sqlite")
cursor = db.cursor()


def requete_emission():
    cursor.execute("""SELECT Pays.nom, sum(quantiteMC02eq) FROM EmissionPays JOIN Pays ON paysProducteur = Pays.idPays  
    WHERE annee = (SELECT MAX(annee) FROM emissionPays) group by Pays.nom""")
    return cursor.fetchall()


def requete_emission_trente_ans():

    cursor.execute("""SELECT Pays.nom,EmissionPays.annee,sum(quantiteMC02eq) FROM EmissionPays JOIN Pays ON EmissionPays.paysProducteur = Pays.idPays 
    group by Pays.nom, EmissionPays.annee
    order by pays.nom, emissionpays.annee""")
    return cursor.fetchall()


def requete_emission_pays_par_activite_continentale(annee):
    cursor.execute("""SELECT Pays.nom,SUM(quantiteMC02eq)/(SELECT emission FROM emissionsMondiales WHERE emissionsMondiales.annee=(?))*100,
    (SELECT emission FROM emissionsMondiales WHERE emissionsMondiales.annee=(?)) 
    FROM EmissionPays INNER JOIN Pays ON paysProducteur = Pays.idPays WHERE annee=(?) GROUP BY Pays.nom """, (str(annee), str(annee), str(annee)))
    return cursor.fetchall()


def requete_PIB_habitant():
    cursor.execute("""select pays.nom, population.annee, sum(PIB.valeur)/sum(population) from PIB
    join Pays on PIB.paysConcerne == Pays.idPays 
    join Population on Pays.idPays = Population.paysAssocie
    group by pays.nom, population.annee
    """)
    return cursor.fetchall()


def requete_Pop():
    cursor.execute("""select pays.nom, population.annee, sum(population) from PIB
    join Pays on PIB.paysConcerne == Pays.idPays 
    join Population on Pays.idPays = Population.paysAssocie
    group by pays.nom, population.annee
    """)
    return cursor.fetchall()

def requete_PIB():
    cursor.execute("""select pays.nom, population.annee, sum(PIB.valeur) from PIB
    join Pays on PIB.paysConcerne == Pays.idPays 
    join Population on Pays.idPays = Population.paysAssocie
    group by pays.nom, population.annee
    """)
    return cursor.fetchall()


def GHG_emissions_par_activité():
    cursor.execute("""
    select pays.nom, activitetype.nom, sum(emissionPays.quantitemc02eq), 100*sum(emissionPays.quantitemc02eq)/(select sum(emission) from emissionsmondiales),
    sum(emissionPays.quantitemc02eq)/(select sum(quantiteEmission) from activitecontinentale)*100, emissionpays.annee from emissionpays
    join pays on pays.idpays = emissionpays.paysproducteur
    join activitetype on emissionpays.typeActivite = activitetype.idactivitetype
    group by pays.nom, activitetype.nom, emissionpays.annee
    order by pays.nom, activiteType.nom, emissionpays.annee
        """)
    return cursor.fetchall()


def production_energie_par_ressource_par_pays():
    cursor.execute("""select ressourceType.nom,ressource.annee, ressource.quantiteEmission, pays.nom
    from ressource 
    join ressourcetype on ressourcetype.idtype = ressource.typeressource 
    join pays on pays.idpays = ressource.produitPar
    where ressource.typeproduction in("produite","Produite")
    group by  pays.nom,ressourcetype.nom, ressource.annee
    """)
    return cursor.fetchall()


def consommation_finale_energie_par_activite():
    cursor.execute("""select activiteType.nom,energieconsommeepays.annee, energieConsommeePays.quantiteMtoe, pays.nom
    from EnergieConsommeePays 
    join activitetype on activitetype.idactivitetype = EnergieConsommeePays.typeActivite 
    join pays on pays.idpays = EnergieConsommeePays.paysProducteur
    group by   activiteType.nom, energieconsommeepays.annee, pays.nom""")
    return cursor.fetchall()


def consommation_finale_energie_par_ressource():
    cursor.execute("""select ressourceType.nom,ressource.annee, ressource.quantiteEmission, pays.nom
    from ressource 
    join ressourcetype on ressourcetype.idtype = ressource.typeressource 
    join pays on pays.idpays = ressource.produitPar
    where ressource.typeproduction in("consomeeFin","ConsomeeFin")
    group by ressourcetype.nom, ressource.annee, pays.nom""")
    return cursor.fetchall()


def consommation_energie_primaire():
    cursor.execute("""select ressourceType.nom,ressource.annee,ressource.quantiteEmission, pays.nom
    from ressource 
    join ressourcetype on ressourcetype.idtype = ressource.typeressource 
    join pays on pays.idpays = ressource.produitPar
    where ressource.typeproduction in("consomee","Consomee")
    group by ressourcetype.nom, ressource.annee, pays.nom""")
    return cursor.fetchall()


def get_country():
    cursor.execute("""SELECT nom FROM Pays""")
    return cursor.fetchall()


'''
print(requete_emission())
print ("\n")
print(requete_emission_trente_ans())
print ("\n")
print(requete_emission_pays_par_activite_continentale(2016))
print ("\n")
print(requete_PIB_habitant())
print ("\nGHG_emissions_par_activité")
print(GHG_emissions_par_activité())
print ("\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\ncomment l'énergie est produite")
print(production_energie_par_ressource_par_pays())
print ("\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\nav")
print(consommation_finale_energie_par_activite())
print ("\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\nav")
print(consommation_finale_energie_par_ressource())
print ("\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\nav")
print(consommation_energie_primaire())
print ("\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\nav")

'''


#cursor.execute("""SELECT SUM(quantiteEmission) FROM ActiviteContinentale WHERE annee=(?)""",("2016",))
# print(cursor.fetchall())
print(production_energie_par_ressource_par_pays())
