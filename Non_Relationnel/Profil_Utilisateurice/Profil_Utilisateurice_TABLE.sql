DROP TYPE IF EXISTS NR_STATUT ;
CREATE TYPE  NR_STATUT AS ENUM ('premium', 'regulier');

CREATE TABLE IF NOT EXISTS NR_Profil_Utilisateurice(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    mail VARCHAR(30) UNIQUE NOT NULL,
    mdp VARCHAR(30) NOT NULL,
    date_inscription DATE NOT NULL,
    statut NR_STATUT NOT NULL,
    genres JSONB
);