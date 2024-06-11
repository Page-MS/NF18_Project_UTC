CREATE TABLE NR_Album(
    id SERIAL primary key,
    titre varchar(30) NOT NULL,
    annee_de_sortie date NOT NULL,
    duree_totale integer NOT NULL,
    artiste_principal REFERENCES NR_Profil_Artiste,
    chansons JSON,
    UNIQUE (titre, artiste_principal)
);