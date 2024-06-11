CREATE TABLE IF NOT EXISTS Album(
    id SERIAL PRIMARY KEY,
    titre VARCHAR(30) NOT NULL,
    annee_de_sortie DATE NOT NULL,
    duree_totale INTEGER NOT NULL,
    artiste_principal INTEGER REFERENCES Profil_Artiste(id) NOT NULL,
    UNIQUE (titre, artiste_principal)
);