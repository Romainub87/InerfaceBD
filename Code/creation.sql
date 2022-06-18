CREATE TABLE Continent (
    idContinent integer PRIMARY KEY AUTOINCREMENT,
    nom varchar(255) NOT NULL UNIQUE
);
CREATE TABLE Pays (
    idPays integer PRIMARY KEY AUTOINCREMENT,
    nom varchar(255) NOT NULL UNIQUE,
    continent integer NOT NULL,
    FOREIGN KEY (continent) REFERENCES Continent(idContinent)
);
CREATE TABLE Population
(
    paysAssocie varchar(255),
    annee       integer,
    population  integer,
    PRIMARY KEY (paysAssocie, annee, population),
    FOREIGN KEY (paysAssocie) REFERENCES Pays(idPays)
);
CREATE TABLE RessourceType(
    idType integer PRIMARY KEY,
    nom varchar(255) NOT NULL
);

CREATE TABLE Ressource(
    idRessource integer PRIMARY KEY AUTOINCREMENT,
    quantiteEmission integer NOT NULL,
    estFossile bit NOT NULL,
    produitPar integer NOT NULL,
    annee integer NOT NULL,
    typeRessource integer NOT NULL,
    typeProduction varchar(255) NOT NULL CHECK(typeProduction IN ("Produite","produite") OR typeProduction IN ("consomee","Consomee")
                      OR typeProduction IN ("consomeeFin","ConsomeeFin")),
    FOREIGN KEY (produitPar) REFERENCES Pays (  idPays),
    FOREIGN KEY (typeRessource) REFERENCES RessourceType(idType)
);
CREATE TABLE EmissionPays
(
    idActivite       integer PRIMARY KEY AUTOINCREMENT,
    quantiteMC02eq integer      NOT NULL,
    annee            integer      NOT NULL,
    paysProducteur   integer,
    typeActivite             integer,-- TODO : Add the NOT NULL command when we will finish the research by types of activites-- .
    FOREIGN KEY (paysProducteur) REFERENCES Pays (idPays),
    FOREIGN KEY (typeActivite) REFERENCES ActiviteType (idActiviteType)
);
CREATE TABLE EnergieConsommeePays
(
    idActiviteConsommee integer PRIMARY KEY AUTOINCREMENT,
    quantiteMtoe integer NOT NULL,
    annee integer NOT NULL,
    paysProducteur   integer,
    typeActivite integer,-- TODO : Add the NOT NULL command when we will finish the research by types of activites-- .
    FOREIGN KEY (paysProducteur) REFERENCES Pays (idPays),
    FOREIGN KEY (typeActivite) REFERENCES ActiviteType (idType)
);
CREATE TABLE ActiviteType
(
    idActiviteType integer PRIMARY KEY,
    nom            varchar(255) NOT NULL UNIQUE
);
CREATE TABLE ActiviteContinentale(
    idActivite integer PRIMARY KEY AUTOINCREMENT,
    quantiteEmission integer NOT NULL,
    annee integer NOT NULL,
    continentProducteur integer,
    FOREIGN KEY (continentProducteur) REFERENCES Continent(idContinent)
);
CREATE TABLE PIB(
        valeur integer,
        annee integer,
        paysConcerne integer NOT NULL,
        FOREIGN KEY (paysConcerne) REFERENCES Pays(idPays),
        PRIMARY KEY (valeur,annee)
);
CREATE TABLE niveauMer(
    idNiveau integer PRIMARY KEY AUTOINCREMENT,
    longitude float not null,
    latitude float not null,
    niveauMer float
);
CREATE TABLE emissionsMondiales(
    annee integer PRIMARY KEY,
    emission integer
);
CREATE TABLE temperature(
    idTemperature integer PRIMARY KEY AUTOINCREMENT,
    longitude float not null,
    latitude float not null,
    temperature float
)
