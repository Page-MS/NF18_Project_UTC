DROP TYPE IF EXISTS NR_AUTORISATION ;

CREATE TYPE NR_AUTORISATION AS ENUM('privee', 'publique', 'partagee_aux_amies');

CREATE TABLE IF NOT EXISTS NR_Playlist(
    id SERIAL PRIMARY KEY,
    titre VARCHAR(60) NOT NULL,
    description VARCHAR(200),
    autorisation_acces NR_AUTORISATION NOT NULL ,
    createurice INTEGER REFERENCES NR_Profil_Artiste,
    chansons JSONB,
    albums JSONB,
    UNIQUE(titre,createurice)
);