DROP TYPE IF EXISTS STATUT ;
CREATE TYPE  STATUT AS ENUM ('premium', 'regulier');

CREATE TABLE IF NOT EXISTS Profil_Utilisateurice(
    id INTEGER REFERENCES Compte PRIMARY KEY,
    mail VARCHAR(30) UNIQUE NOT NULL,
    mdp VARCHAR(30) NOT NULL,
    date_inscription DATE NOT NULL,
    statut STATUT NOT NULL
);