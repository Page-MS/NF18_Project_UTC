DROP TYPE IF EXISTS STATUT ;
CREATE TYPE  STATUT AS ENUM ('premium', 'regulier');

CREATE TABLE NR_Profil_Utilisateurice(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    mail VARCHAR(30) UNIQUE NOT NULL,
    mdp VARCHAR(30) NOT NULL,
    date_inscription DATE NOT NULL,
    statut STATUT NOT NULL,
    genres JSONB,
);