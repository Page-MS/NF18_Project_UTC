CREATE TABLE Album(
    id integer primary key,
    titre varchar(30) NOT NULL,
    annee_de_sortie date NOT NULL,
    duree_totale integer NOT NULL,
    artiste_principal integer references Profil_Artiste(id) NOT NULL,
    UNIQUE (titre, artiste_principal)
);