from ssl import PROTOCOL_TLSv1_1
from matplotlib import pyplot as plt
import pandas as pd
import sqlite3
import numpy as np
from CreaGraphe import *
import selection as slt


db = sqlite3.connect("base.sqlite")
cursor = db.cursor()


def CreationImage():
    plot_base_evolution(slt.requete_emission_trente_ans(), "année", "Emission")
    plt.savefig("Interface/ImageGen/Emission30ans.png")
    plt.close()

    piechart_base_on_year(slt.requete_emission_pays_par_activite_continentale(
        1990), "")
    plt.savefig("Interface/ImageGen/EmissionPaysParActivite.png")
    plt.close()
    plot_base_on_year(slt.requete_emission(),
                      "Émissions de gaz à effet de serre en MTCO2eq")
    plt.savefig("Interface/ImageGen/EmissionTotale.png")
    plt.close()

    plot_base_evolution(slt.requete_PIB_habitant(),  "Année", "Montant")
    plt.title("Évolution du PIB/Habitant sur les 30 dernières années")
    plt.tight_layout()
    plt.savefig("Interface/ImageGen/PIB.Hab.png")
    plt.close()

    plot_base_evolution(slt.requete_Pop(), "Année", "Montant")
    plt.title("Évolution population 30 dernières années")
    plt.savefig("Interface/ImageGen/Population.png")
    plt.close()

    plot_base_evolution(slt.requete_PIB(), "Année", "Montant")
    plt.title("Évolution PIB 30 dernières années")
    plt.savefig("Interface/ImageGen/PIB.png")
    plt.close()

    piechart_base_on_year(slt.requete_emission_pays_par_activite_continentale(
        2016), "")
    plt.savefig("Interface/ImageGen/EmissionEmissionPaysParRapportAuxAutre.png")
    plt.close()

    for i in slt.get_country():
        plot_base_evolution(get_ressource_for_one_country(slt.production_energie_par_ressource_par_pays(
        ), i[0]), "Année", "Pollution par ressource, en Mtoe", i[0])
        plt.savefig("Interface/ImageGen/Evo" + i[0] + ".png")
        plt.close()

    plt.close()

    for i in slt.get_country():
        plot_base_evolution(get_ressource_for_one_country(slt.consommation_finale_energie_par_activite(
        ), i[0]), "Année", "Consommation finale par activité", i[0])
        plt.savefig("Interface/ImageGen/Conso" + i[0] + ".png")
        plt.close()
    """
    for i in slt.get_country():
        plot_base_evolution(get_ressource_for_one_country(slt.GHG_emissions_par_activité(
        ), i[0]), "Année", "Émission de gaz à effet de serre", i[0])
        plt.close()
    """
