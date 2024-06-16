CREATE TABLE IF NOT EXISTS NR_Album(
    id SERIAL PRIMARY KEY,
    titre VARCHAR(30) NOT NULL,
    annee_de_sortie DATE NOT NULL,
    artiste_principal INTEGER REFERENCES NR_Profil_Artiste,
    chansons JSON,
    UNIQUE (titre, artiste_principal)
);